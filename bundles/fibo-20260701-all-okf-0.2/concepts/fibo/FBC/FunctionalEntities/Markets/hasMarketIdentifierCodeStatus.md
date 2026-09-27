---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has market identifier code status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the status of a specific market identifier code (MIC)
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasMarketIdentifierCodeStatus
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: has market identifier code status
type: Ontology Property
---

# has market identifier code status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasMarketIdentifierCodeStatus>

## Definition

indicates the status of a specific market identifier code (MIC)

## Relationships

- **Range**: [MarketIdentifierCodeStatus](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus.md)
- **Subproperty of**: [hasRegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus.md)

## Annotations

- **label**: has market identifier code status
- **definition**: indicates the status of a specific market identifier code (MIC)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
