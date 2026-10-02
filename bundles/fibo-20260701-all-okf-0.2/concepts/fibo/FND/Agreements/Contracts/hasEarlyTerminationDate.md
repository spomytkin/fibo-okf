---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has early termination date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a termination date that occurs prior to an explicit expiration date
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasTerminationDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEarlyTerminationDate
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has early termination date
type: Ontology Property
---

# has early termination date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEarlyTerminationDate>

## Definition

indicates a termination date that occurs prior to an explicit expiration date

## Relationships

- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasTerminationDate](/concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md)

## Annotations

- **label** (en): has early termination date
- **definition** (en): indicates a termination date that occurs prior to an explicit expiration date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
