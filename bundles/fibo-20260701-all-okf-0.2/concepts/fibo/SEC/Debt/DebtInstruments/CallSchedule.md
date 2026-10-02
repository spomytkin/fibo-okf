---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: call schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a schedule of call prices and when they are in effect
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: Nd47a7e0c476047f9a5d735996b012332
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallSchedule
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: call schedule
type: Ontology Class
---

# call schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallSchedule>

## Definition

a schedule of call prices and when they are in effect

## Relationships

- **Subclass of**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `Nd47a7e0c476047f9a5d735996b012332`
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [CallEvent](/concepts/fibo/SEC/Debt/DebtInstruments/CallEvent.md)

## Annotations

- **label**: call schedule
- **definition**: a schedule of call prices and when they are in effect

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
