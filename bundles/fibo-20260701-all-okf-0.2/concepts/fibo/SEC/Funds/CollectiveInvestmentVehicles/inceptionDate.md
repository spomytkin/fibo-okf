---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inception date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Authorization date in the country of origin.
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/inceptionDate
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: inception date
type: Ontology Property
---

# inception date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/inceptionDate>

## Definition

Authorization date in the country of origin.

## Relationships

- **Domain**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): inception date
- **definition** (en): Authorization date in the country of origin.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
