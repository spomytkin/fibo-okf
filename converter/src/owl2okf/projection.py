"""Project semantic IR objects into a small, explicit OKF bundle model."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import PurePosixPath
from urllib.parse import urlsplit

from .profiles.base import OntologyProfile
from .semantic import OntologyEntity, OntologyModel


@dataclass(frozen=True)
class OKFDocument:
    path: str
    frontmatter: dict
    body: str


@dataclass
class OKFProjection:
    profile_name: str
    profile_version: str
    scope: str
    documents: dict[str, OKFDocument]
    entity_paths: dict[str, str]


def _assign_paths(entities: list[OntologyEntity], profile: OntologyProfile) -> dict[str, str]:
    candidates: dict[str, list[OntologyEntity]] = {}
    for entity in entities:
        candidates.setdefault(profile.path_for(entity), []).append(entity)
    paths = {}
    for path, collisions in candidates.items():
        if len(collisions) == 1:
            paths[collisions[0].iri] = path
            continue
        for entity in collisions:
            suffix = hashlib.sha256(entity.iri.encode("utf-8")).hexdigest()[:10]
            candidate = PurePosixPath(path)
            paths[entity.iri] = (candidate.parent / f"{candidate.stem}--{suffix}{candidate.suffix}").as_posix()
    return paths


def _relationship_frontmatter(entity: OntologyEntity, profile: OntologyProfile, paths: dict[str, str]) -> dict:
    owl: dict = {}
    for relation in entity.relations:
        kind = profile.relationship_kind(relation.predicate)
        targets = owl.setdefault(kind, [])
        target = {"resource": relation.target, "predicate": relation.predicate}
        if relation.target in paths:
            target["concept"] = f"/{paths[relation.target]}"
        targets.append(target)
    for kind in owl:
        owl[kind].sort(key=lambda item: (item["resource"], item.get("concept", ""), item["predicate"]))
    if entity.restrictions:
        owl["restrictions"] = [
            {
                "property": item.property,
                "kind": item.kind,
                **({"cardinality": item.cardinality} if item.cardinality is not None else {}),
                **({"filler": item.filler} if item.filler is not None else {}),
                **({"value": item.value} if item.value is not None else {}),
            }
            for item in entity.restrictions
        ]
    if entity.characteristics:
        owl["characteristics"] = entity.characteristics
    if entity.deprecated:
        owl["deprecated"] = True
    if entity.rdf_types:
        owl["rdf_types"] = entity.rdf_types
    if entity.annotations:
        owl["annotations"] = [
            {
                "predicate": annotation.predicate,
                "value": annotation.value,
                **({"language": annotation.language} if annotation.language else {}),
                **({"datatype": annotation.datatype} if annotation.datatype else {}),
            }
            for annotation in entity.annotations
        ]
    return owl


def _source_frontmatter(entity: OntologyEntity, model: OntologyModel) -> list[dict[str, str]]:
    sources = {source.path: source for source in model.source_files}
    result = []
    for path in entity.source_paths:
        source = sources.get(path)
        if source is None:
            continue
        result.append({
            "id": f"fibo-source-{source.sha256[:10]}",
            "resource": f"references/fibo/{source.path}",
            "title": f"FIBO source {source.path}",
            "sha256": source.sha256,
        })
    return sorted(result, key=lambda item: item["resource"])


def _markdown_link(target: str, label: str, paths: dict[str, str]) -> str:
    if target in paths:
        return f"[{label}](/{paths[target]})"
    return f"[{label}](<{target}>)"


def _title_for_target(target: str) -> str:
    parsed = urlsplit(target)
    return parsed.fragment or parsed.path.rstrip("/").rsplit("/", 1)[-1] or target


def _render_body(entity: OntologyEntity, profile: OntologyProfile, paths: dict[str, str]) -> str:
    title = profile.title_for(entity)
    lines = [f"# {title}", "", f"Canonical resource: <{entity.iri}>"]
    definitions = profile.definition_for(entity)
    if definitions:
        lines.extend(["", "## Definition", "", definitions[0]])
        if len(definitions) > 1:
            lines.extend(["", "## Additional definitions", "", *[f"- {item}" for item in definitions[1:]]])
    synonyms = profile.synonyms_for(entity)
    if synonyms:
        lines.extend(["", "## Synonyms", "", *[f"- {value}" for value in synonyms]])
    linked = [relation for relation in entity.relations if profile.relationship_kind(relation.predicate) != "disjoint_with"]
    constraints = [relation for relation in entity.relations if profile.relationship_kind(relation.predicate) == "disjoint_with"]
    if linked:
        lines.extend(["", "## Relationships", ""])
        for relation in linked:
            kind = profile.relationship_kind(relation.predicate).replace("_", " ").capitalize()
            lines.append(f"- **{kind}**: {_markdown_link(relation.target, _title_for_target(relation.target), paths)}")
    if constraints or entity.restrictions:
        lines.extend(["", "## Constraints", ""])
        for relation in constraints:
            lines.append(f"- **Disjoint with**: {_markdown_link(relation.target, _title_for_target(relation.target), paths)}")
        for restriction in entity.restrictions:
            prop = _markdown_link(restriction.property, _title_for_target(restriction.property), paths)
            value = restriction.kind.replace("_", " ")
            if restriction.cardinality is not None:
                value += f" {restriction.cardinality}"
            if restriction.filler:
                value += f" of type {_markdown_link(restriction.filler, _title_for_target(restriction.filler), paths)}"
            if restriction.value:
                value += f" value `{restriction.value}`"
            lines.append(f"- **{prop}**: {value}")
    if entity.annotations:
        lines.extend(["", "## Annotations", ""])
        for annotation in entity.annotations:
            label = _title_for_target(annotation.predicate)
            language = f" ({annotation.language})" if annotation.language else ""
            lines.append(f"- **{label}**{language}: {annotation.value.replace(chr(10), ' ').replace(chr(13), ' ')}")
    lines.extend([
        "",
        "## Source fidelity",
        "",
        "The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def project(model: OntologyModel, profile: OntologyProfile, *, scope: str = "all") -> OKFProjection:
    selected = [entity for entity in model.entities.values() if profile.select(entity)]
    if scope.lower() not in {"all", "domains"}:
        domain = scope.upper()
        selected = [entity for entity in selected if "/ontology/" + domain + "/" in entity.iri]
        if not selected:
            raise ValueError(f"No entities matched requested scope {domain!r}")
    paths = _assign_paths(selected, profile)
    documents = {}
    for entity in sorted(selected, key=lambda item: item.iri):
        frontmatter = {
            "type": profile.type_for(entity),
            "title": profile.title_for(entity),
            "resource": entity.iri,
            "owl": _relationship_frontmatter(entity, profile, paths),
        }
        if entity.source_paths:
            frontmatter["sources"] = _source_frontmatter(entity, model)
        document_path = paths[entity.iri]
        documents[document_path] = OKFDocument(
            path=document_path,
            frontmatter=frontmatter,
            body=_render_body(entity, profile, paths),
        )
    return OKFProjection(
        profile_name=profile.name,
        profile_version=profile.version,
        scope=scope.upper() if scope.lower() not in {"all", "domains"} else scope.lower(),
        documents=documents,
        entity_paths=paths,
    )
