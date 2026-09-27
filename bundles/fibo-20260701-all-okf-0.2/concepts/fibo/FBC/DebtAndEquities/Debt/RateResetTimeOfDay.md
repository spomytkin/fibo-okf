---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rate reset time of day
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: time of day that an interest rate is reset, as indicated by some interest rate authority or market data provider
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include certain rates published by the Federal Reserve Board in their H.15 schedule, which are published
      at 4:15 pm on business days that are not holidays in the US.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/BusinessCenter
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasBusinessCenter
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/TimeOfDay
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RateResetTimeOfDay
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: rate reset time of day
type: Ontology Class
---

# rate reset time of day

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RateResetTimeOfDay>

## Definition

time of day that an interest rate is reset, as indicated by some interest rate authority or market data provider

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [TimeOfDay](<https://www.omg.org/spec/Commons/DatesAndTimes/TimeOfDay>)

## Constraints

- **[hasBusinessCenter](<https://www.omg.org/spec/Commons/Locations/hasBusinessCenter>)**: min qualified cardinality 0 of type [BusinessCenter](<https://www.omg.org/spec/Commons/Locations/BusinessCenter>)

## Annotations

- **label**: rate reset time of day
- **definition**: time of day that an interest rate is reset, as indicated by some interest rate authority or market data provider
- **example**: Examples include certain rates published by the Federal Reserve Board in their H.15 schedule, which are published at 4:15 pm on business days that are not holidays in the US.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
