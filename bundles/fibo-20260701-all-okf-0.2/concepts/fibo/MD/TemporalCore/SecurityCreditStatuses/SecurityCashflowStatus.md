---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security cashflow status
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The status of the cashflow due to the holder from the security.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Specialize this for preferred stocks, debt tranches and so on.
  disjoint_with:
  - concept: /concepts/fibo/MD/TemporalCore/SecurityCreditStatuses/SecurityCreditStatus.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/SecurityCreditStatus
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStatus
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/SecurityCashflowStatus
sources:
- id: fibo-source-e03c8b200b
  resource: references/fibo/MD/TemporalCore/SecurityCreditStatuses.rdf
  sha256: e03c8b200b6a5c2725a08112c4d0ae2e6d50d0fb9df0b05784ec7b794efce940
  title: FIBO source MD/TemporalCore/SecurityCreditStatuses.rdf
title: security cashflow status
type: Ontology Class
---

# security cashflow status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityCreditStatuses/SecurityCashflowStatus>

## Definition

The status of the cashflow due to the holder from the security.

## Relationships

- **Subclass of**: [LifecycleStatus](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStatus.md)

## Constraints

- **Disjoint with**: [SecurityCreditStatus](/concepts/fibo/MD/TemporalCore/SecurityCreditStatuses/SecurityCreditStatus.md)

## Annotations

- **label** (en): security cashflow status
- **definition** (en): The status of the cashflow due to the holder from the security.
- **editorialNote** (en): Specialize this for preferred stocks, debt tranches and so on.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
