---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has intended liquidation date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links an agreement, contract, or legal entity to a date on which it is scheduled to be sold
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasTerminationDate
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/hasIntendedLiquidationDate
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: has intended liquidation date
type: Ontology Property
---

# has intended liquidation date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/hasIntendedLiquidationDate>

## Definition

links an agreement, contract, or legal entity to a date on which it is scheduled to be sold

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasTerminationDate](/concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md)

## Annotations

- **label** (en): has intended liquidation date
- **definition** (en): links an agreement, contract, or legal entity to a date on which it is scheduled to be sold

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
