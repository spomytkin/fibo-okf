---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: when issued
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: When Issued or Gray Market trading is when a security is traded ahead of the date at which it is to be issued.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/SecurityLifecycleStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/SecurityLifecycleStatus
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/WhenIssued
sources:
- id: fibo-source-8a03a65ade
  resource: references/fibo/MD/TemporalCore/SecurityTradingStatuses.rdf
  sha256: 8a03a65aded2ec980c264825a2bc807c16de2c9eaf269f974fefbf8780f0ad23
  title: FIBO source MD/TemporalCore/SecurityTradingStatuses.rdf
title: when issued
type: Ontology Class
---

# when issued

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/WhenIssued>

## Definition

When Issued or Gray Market trading is when a security is traded ahead of the date at which it is to be issued.

## Relationships

- **Subclass of**: [SecurityLifecycleStatus](/concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/SecurityLifecycleStatus.md)

## Annotations

- **label** (en): when issued
- **definition** (en): When Issued or Gray Market trading is when a security is traded ahead of the date at which it is to be issued.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
