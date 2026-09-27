---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has price and yield day count convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the convention used to determine the number of days in a month and days in a year that are counted when
      performing calculations for yield and price figures
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/DayCountConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasPriceAndYieldDayCountConvention
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: has price and yield day count convention
type: Ontology Property
---

# has price and yield day count convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasPriceAndYieldDayCountConvention>

## Definition

indicates the convention used to determine the number of days in a month and days in a year that are counted when performing calculations for yield and price figures

## Relationships

- **Range**: [DayCountConvention](/concepts/fibo/FBC/DebtAndEquities/Debt/DayCountConvention.md)
- **Subproperty of**: [hasBusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessRecurrenceIntervalConvention.md)

## Annotations

- **label**: has price and yield day count convention
- **definition**: indicates the convention used to determine the number of days in a month and days in a year that are counted when performing calculations for yield and price figures

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
