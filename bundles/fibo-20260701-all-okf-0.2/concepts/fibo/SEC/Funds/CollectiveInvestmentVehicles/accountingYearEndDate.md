---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: accounting year end date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Last day of the accounting year for the fund.
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/accountingYearEndDate
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: accounting year end date
type: Ontology Property
---

# accounting year end date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/accountingYearEndDate>

## Definition

Last day of the accounting year for the fund.

## Relationships

- **Range**: [DayOfMonth](/concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)

## Annotations

- **label** (en): accounting year end date
- **definition** (en): Last day of the accounting year for the fund.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
