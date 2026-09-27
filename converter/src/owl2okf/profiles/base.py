"""Shared protocol for domain profiles."""

from __future__ import annotations

from typing import Protocol

from ..semantic import OntologyEntity


class OntologyProfile(Protocol):
    name: str
    version: str

    def select(self, entity: OntologyEntity) -> bool: ...

    def type_for(self, entity: OntologyEntity) -> str: ...

    def path_for(self, entity: OntologyEntity) -> str: ...

    def title_for(self, entity: OntologyEntity) -> str: ...

    def definition_for(self, entity: OntologyEntity) -> list[str]: ...

    def synonyms_for(self, entity: OntologyEntity) -> list[str]: ...

    def relationship_kind(self, predicate: str) -> str: ...
