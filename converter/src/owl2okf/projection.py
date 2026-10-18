"""Project semantic IR objects into a small, explicit OKF bundle model."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import PurePosixPath
from urllib.parse import urlsplit

from . import __version__
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
    return owl


def _source_frontmatter(
    entity: OntologyEntity,
    model: OntologyModel,
    source_credibility: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    sources = {source.path: source for source in model.source_files}
    result = []
    for path in entity.source_paths:
        source = sources.get(path)
        if source is None:
            continue
        entry = {
            "id": f"fibo-source-{source.sha256[:10]}",
            "resource": f"references/fibo/{source.path}",
            "title": f"FIBO source {source.path}",
            "sha256": source.sha256,
        }
        entry.update(source_credibility.get(path, {}))
        result.append(entry)
    return sorted(result, key=lambda item: item["resource"])


def _tags_for(entity: OntologyEntity, profile: OntologyProfile) -> list[str]:
    """Use the ontology module path as stable, cross-document tags."""
    namespace = getattr(profile, "namespace", "")
    namespace_path = urlsplit(namespace).path.rstrip("/") + "/"
    parsed = urlsplit(entity.iri)
    if not namespace_path or not parsed.path.startswith(namespace_path):
        return []
    parts = parsed.path[len(namespace_path):].strip("/").split("/")
    if parts and len(parts[0]) == 8 and parts[0].isdigit():
        parts = parts[1:]
    return parts[:-1]


def _direct_subclasses(
    entity: OntologyEntity,
    entities: dict[str, OntologyEntity],
    profile: OntologyProfile,
    paths: dict[str, str],
) -> list[dict[str, str]]:
    children = []
    for candidate in entities.values():
        for relation in candidate.relations:
            if relation.target == entity.iri and profile.relationship_kind(relation.predicate) == "subclass_of":
                children.append({
                    "resource": candidate.iri,
                    "predicate": relation.predicate,
                    "concept": f"/{paths[candidate.iri]}",
                    "title": profile.title_for(candidate),
                })
    return sorted(children, key=lambda item: (item["title"].casefold(), item["resource"]))


def _markdown_link(target: str, label: str, paths: dict[str, str]) -> str:
    if target in paths:
        return f"[{label}](/{paths[target]})"
    return f"[{label}](<{target}>)"


def _title_for_target(target: str) -> str:
    parsed = urlsplit(target)
    return parsed.fragment or parsed.path.rstrip("/").rsplit("/", 1)[-1] or target


def _render_body(
    entity: OntologyEntity,
    profile: OntologyProfile,
    paths: dict[str, str],
    direct_subclasses: list[dict[str, str]],
) -> str:
    title = profile.title_for(entity)
    lines = [f"# {title}"]
    definitions = profile.definition_for(entity)
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
    if direct_subclasses:
        lines.extend(["", "## Direct subclasses", ""])
        for child in direct_subclasses:
            lines.append(f"- [{child['title']}]({child['concept']})")
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
    return "\n".join(lines).rstrip() + "\n"


def project(
    model: OntologyModel,
    profile: OntologyProfile,
    *,
    scope: str = "all",
    source_credibility: dict[str, dict[str, str]] | None = None,
) -> OKFProjection:
    selected = [entity for entity in model.entities.values() if profile.select(entity)]
    if scope.lower() not in {"all", "domains"}:
        domain = scope.upper()
        selected = [entity for entity in selected if "/ontology/" + domain + "/" in entity.iri]
        if not selected:
            raise ValueError(f"No entities matched requested scope {domain!r}")
    paths = _assign_paths(selected, profile)
    selected_by_iri = {entity.iri: entity for entity in selected}
    documents = {}
    for entity in sorted(selected, key=lambda item: item.iri):
        definitions = profile.definition_for(entity)
        direct_subclasses = _direct_subclasses(entity, selected_by_iri, profile, paths)
        frontmatter = {
            "title": profile.title_for(entity),
            "type": profile.type_for(entity),
        }
        if definitions:
            frontmatter["description"] = definitions[0]
        frontmatter["resource"] = entity.iri
        tags = _tags_for(entity, profile)
        if tags:
            frontmatter["tags"] = tags
        frontmatter["generated"] = {"by": f"owl2okf/{__version__}"}
        if entity.source_paths:
            frontmatter["sources"] = _source_frontmatter(entity, model, source_credibility or {})
        owl = _relationship_frontmatter(entity, profile, paths)
        if direct_subclasses:
            owl["direct_subclasses"] = [
                {key: value for key, value in child.items() if key != "title"}
                for child in direct_subclasses
            ]
        frontmatter["owl"] = owl
        document_path = paths[entity.iri]
        documents[document_path] = OKFDocument(
            path=document_path,
            frontmatter=frontmatter,
            body=_render_body(entity, profile, paths, direct_subclasses),
        )
    return OKFProjection(
        profile_name=profile.name,
        profile_version=profile.version,
        scope=scope.upper() if scope.lower() not in {"all", "domains"} else scope.lower(),
        documents=documents,
        entity_paths=paths,
    )
