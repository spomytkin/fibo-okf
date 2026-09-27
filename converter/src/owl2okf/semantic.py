"""RDF-to-OWL semantic intermediate representation."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SourceFile:
    path: str
    format: str
    sha256: str


@dataclass(frozen=True)
class Relationship:
    kind: str
    predicate: str
    target: str


@dataclass(frozen=True)
class Restriction:
    property: str
    kind: str
    cardinality: int | None = None
    filler: str | None = None
    value: str | None = None


@dataclass(frozen=True)
class Annotation:
    predicate: str
    value: str
    language: str | None = None
    datatype: str | None = None


@dataclass
class OntologyEntity:
    iri: str
    kind: str
    rdf_types: list[str] = field(default_factory=list)
    deprecated: bool = False
    relations: list[Relationship] = field(default_factory=list)
    restrictions: list[Restriction] = field(default_factory=list)
    characteristics: list[str] = field(default_factory=list)
    annotations: list[Annotation] = field(default_factory=list)
    source_paths: list[str] = field(default_factory=list)


@dataclass
class OntologyModel:
    entities: dict[str, OntologyEntity]
    source_files: list[SourceFile]
    version_iris: list[str]
    imports: list[str]
    triple_count: int
    unsupported: Counter[str] = field(default_factory=Counter)
    warnings: list[dict[str, str]] = field(default_factory=list)
    options: dict[str, Any] = field(default_factory=dict)
