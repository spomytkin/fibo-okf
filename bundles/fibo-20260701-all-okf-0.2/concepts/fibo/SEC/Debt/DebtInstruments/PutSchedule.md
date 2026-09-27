---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: put schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a schedule that defines the events associated with the put feature of a debt instrument, i.e, the dates on which
      the debt instrument may be sold at what price by the holder
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
    value: Nb1c5449bc24f41a4912bc6b0f6d54081
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutSchedule
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: put schedule
type: Ontology Class
---

# put schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutSchedule>

## Definition

a schedule that defines the events associated with the put feature of a debt instrument, i.e, the dates on which the debt instrument may be sold at what price by the holder

## Relationships

- **Subclass of**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from value `Nb1c5449bc24f41a4912bc6b0f6d54081`
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [PutEvent](/concepts/fibo/SEC/Debt/DebtInstruments/PutEvent.md)

## Annotations

- **label**: put schedule
- **definition**: a schedule that defines the events associated with the put feature of a debt instrument, i.e, the dates on which the debt instrument may be sold at what price by the holder

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
