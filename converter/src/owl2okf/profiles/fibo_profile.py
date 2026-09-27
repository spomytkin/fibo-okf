"""Configuration-backed FIBO projection profile."""

from __future__ import annotations

import hashlib
import re
from importlib.resources import files
from pathlib import PurePosixPath
from urllib.parse import unquote, urlsplit

import yaml

from ..semantic import OntologyEntity


def _slug(text: str) -> str:
    text = unquote(text)
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip(".-_")
    return (slug or "unnamed")[:64]


class FiboProfile:
    def __init__(self) -> None:
        package_file = files("owl2okf.profiles.fibo").joinpath("profile.yaml")
        self.config = yaml.safe_load(package_file.read_text(encoding="utf-8"))
        self.name = self.config["name"]
        self.version = str(self.config["version"])
        self.namespace = self.config["namespace"]
        self._title_predicates = self.config["title_predicates"]
        self._definition_predicates = self.config["definition_predicates"]
        self._synonym_predicates = self.config["synonym_predicates"]
        self._entity_types = self.config["entity_types"]
        self._relationship_predicates = self.config["relationship_predicates"]
        self._included = set(self.config["included_entity_kinds"])

    def select(self, entity: OntologyEntity) -> bool:
        return entity.iri.startswith(self.namespace) and entity.kind in self._included

    def type_for(self, entity: OntologyEntity) -> str:
        return self._entity_types.get(entity.kind, "Ontology Entity")

    def path_for(self, entity: OntologyEntity) -> str:
        parts = urlsplit(entity.iri).path[len(urlsplit(self.namespace).path):].strip("/").split("/")
        if parts and re.fullmatch(r"\d{8}", parts[0]):
            parts = parts[1:]
        if len(parts) > 1 and re.fullmatch(r"\d{8}", parts[1]):
            parts = [parts[0], *parts[2:]]
        fragment = urlsplit(entity.iri).fragment
        if fragment:
            parts.append(fragment)
        if not parts:
            parts = [hashlib.sha256(entity.iri.encode("utf-8")).hexdigest()[:12]]
        safe = [_slug(part) for part in parts]
        leaf = safe[-1]
        return (PurePosixPath("concepts") / "fibo" / PurePosixPath(*safe[:-1]) / f"{leaf}.md").as_posix()

    def _annotation_values(self, entity: OntologyEntity, predicates: list[str]) -> list[str]:
        values = []
        for predicate in predicates:
            matching = [annotation for annotation in entity.annotations if annotation.predicate == predicate]
            matching.sort(key=lambda annotation: (0 if (annotation.language or "").lower() == "en" else 1 if not annotation.language else 2, annotation.value.casefold(), annotation.value))
            values.extend(annotation.value.strip() for annotation in matching if annotation.value.strip())
        return list(dict.fromkeys(values))

    def title_for(self, entity: OntologyEntity) -> str:
        values = self._annotation_values(entity, self._title_predicates)
        if values:
            return values[0]
        local = urlsplit(entity.iri).fragment or urlsplit(entity.iri).path.rstrip("/").rsplit("/", 1)[-1]
        return unquote(local or "Unnamed ontology entity")

    def definition_for(self, entity: OntologyEntity) -> list[str]:
        return self._annotation_values(entity, self._definition_predicates)

    def synonyms_for(self, entity: OntologyEntity) -> list[str]:
        return self._annotation_values(entity, self._synonym_predicates)

    def relationship_kind(self, predicate: str) -> str:
        return self._relationship_predicates.get(predicate, "related_to")


class GenericProfile:
    name = "generic"
    version = "0.1.0"

    def select(self, entity: OntologyEntity) -> bool:
        return entity.kind != "entity"

    def type_for(self, entity: OntologyEntity) -> str:
        names = {
            "class": "Ontology Class",
            "object_property": "Ontology Property",
            "datatype_property": "Ontology Property",
            "annotation_property": "Ontology Property",
            "property": "Ontology Property",
            "individual": "Ontology Individual",
            "ontology": "Ontology Definition",
            "concept": "Ontology Concept",
        }
        return names.get(entity.kind, "Ontology Entity")

    def path_for(self, entity: OntologyEntity) -> str:
        parsed = urlsplit(entity.iri)
        host = _slug(parsed.netloc.lower())
        local = parsed.fragment or parsed.path.rstrip("/").rsplit("/", 1)[-1]
        stable = hashlib.sha256(entity.iri.encode("utf-8")).hexdigest()[:10]
        return (PurePosixPath("concepts") / host / f"{_slug(local)}--{stable}.md").as_posix()

    def _values(self, entity: OntologyEntity, suffix: str) -> list[str]:
        return sorted({annotation.value.strip() for annotation in entity.annotations if annotation.predicate.endswith(suffix) and annotation.value.strip()}, key=str.casefold)

    def title_for(self, entity: OntologyEntity) -> str:
        return (self._values(entity, "prefLabel") + self._values(entity, "label") or [urlsplit(entity.iri).path.rsplit("/", 1)[-1]])[0]

    def definition_for(self, entity: OntologyEntity) -> list[str]:
        return self._values(entity, "definition") + self._values(entity, "comment")

    def synonyms_for(self, entity: OntologyEntity) -> list[str]:
        return self._values(entity, "altLabel")

    def relationship_kind(self, predicate: str) -> str:
        return {
            "http://www.w3.org/2000/01/rdf-schema#subClassOf": "subclass_of",
            "http://www.w3.org/2002/07/owl#equivalentClass": "equivalent_to",
            "http://www.w3.org/2002/07/owl#disjointWith": "disjoint_with",
        }.get(predicate, "related_to")


def get_profile(name: str):
    if name.lower() == "fibo":
        return FiboProfile()
    if name.lower() == "generic":
        return GenericProfile()
    raise ValueError(f"Unknown profile {name!r}; available profiles: fibo, generic")
