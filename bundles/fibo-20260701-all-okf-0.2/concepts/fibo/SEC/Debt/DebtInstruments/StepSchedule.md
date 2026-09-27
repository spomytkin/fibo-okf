---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: step schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule specifying the date(s) and change in a contractual term(s), e.g., rate or notional amount, for a contract
      that has a feature where stipulated changes occur at specified intervals or on specified dates
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepSchedule
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: step schedule
type: Ontology Class
---

# step schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepSchedule>

## Definition

schedule specifying the date(s) and change in a contractual term(s), e.g., rate or notional amount, for a contract that has a feature where stipulated changes occur at specified intervals or on specified dates

## Relationships

- **Subclass of**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [StepEvent](/concepts/fibo/SEC/Debt/DebtInstruments/StepEvent.md)

## Annotations

- **label**: step schedule
- **definition**: schedule specifying the date(s) and change in a contractual term(s), e.g., rate or notional amount, for a contract that has a feature where stipulated changes occur at specified intervals or on specified dates

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
