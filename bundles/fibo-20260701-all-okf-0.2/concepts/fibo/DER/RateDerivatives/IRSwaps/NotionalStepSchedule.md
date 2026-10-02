---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: notional step schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule of changes in the notional amount on which interest is paid, comprising the regular sequence of step events
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepPeriodLength
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/StepSchedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepSchedule
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepSchedule
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: notional step schedule
type: Ontology Class
---

# notional step schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/NotionalStepSchedule>

## Definition

schedule of changes in the notional amount on which interest is paid, comprising the regular sequence of step events

## Relationships

- **Subclass of**: [ProjectedContractEventSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/ProjectedContractEventSchedule.md)
- **Subclass of**: [StepSchedule](/concepts/fibo/SEC/Debt/DebtInstruments/StepSchedule.md)

## Constraints

- **[hasRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md)**: some values from of type [NotionalStepPeriodLength](/concepts/fibo/DER/RateDerivatives/IRSwaps/NotionalStepPeriodLength.md)
- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: some values from of type [NotionalStepChangeEvent](/concepts/fibo/DER/RateDerivatives/IRSwaps/NotionalStepChangeEvent.md)

## Annotations

- **label**: notional step schedule
- **definition**: schedule of changes in the notional amount on which interest is paid, comprising the regular sequence of step events

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
