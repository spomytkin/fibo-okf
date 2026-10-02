---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: step event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event that prescribes a change in a contractual term, such as a rate or notional amount, for a given contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/CalculationEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/CalculationEvent
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/PrescriptiveEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PrescriptiveEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepEvent
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: step event
type: Ontology Class
---

# step event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/StepEvent>

## Definition

event that prescribes a change in a contractual term, such as a rate or notional amount, for a given contract

## Relationships

- **Subclass of**: [CalculationEvent](/concepts/fibo/FND/DatesAndTimes/Occurrences/CalculationEvent.md)
- **Subclass of**: [PrescriptiveEvent](/concepts/fibo/SEC/Debt/DebtInstruments/PrescriptiveEvent.md)

## Annotations

- **label**: step event
- **definition**: event that prescribes a change in a contractual term, such as a rate or notional amount, for a given contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
