---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: end of fiscal year
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Day and month on any given year at which the books are closed and profit and loss is determined.
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/endOfFiscalYear
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: end of fiscal year
type: Ontology Property
---

# end of fiscal year

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/endOfFiscalYear>

## Definition

Day and month on any given year at which the books are closed and profit and loss is determined.

## Relationships

- **Range**: [DayOfMonth](/concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)

## Annotations

- **label** (en): end of fiscal year
- **definition** (en): Day and month on any given year at which the books are closed and profit and loss is determined.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
