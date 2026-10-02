---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trading date rule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convention for determining trading dates defined with reference to some trading date calendar published by some
      trading facility or exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Corresponds to several ISDA FpML enumeration entries for determining Calculation Date, but refers to other kinds
      of trading date defined in those calendars. These include Canadian, Australian and New Zealand dates. Note also that
      some of these have roll rules included within them for when the date determined by the specification returns a non working
      day, while others explicitly return a business day and require no date roll rule. At least one is silent on this matter.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/TradingDateRule
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: trading date rule
type: Ontology Class
---

# trading date rule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/TradingDateRule>

## Definition

convention for determining trading dates defined with reference to some trading date calendar published by some trading facility or exchange

## Relationships

- **Subclass of**: [BusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)

## Annotations

- **label**: trading date rule
- **definition**: convention for determining trading dates defined with reference to some trading date calendar published by some trading facility or exchange
- **explanatoryNote**: Corresponds to several ISDA FpML enumeration entries for determining Calculation Date, but refers to other kinds of trading date defined in those calendars. These include Canadian, Australian and New Zealand dates. Note also that some of these have roll rules included within them for when the date determined by the specification returns a non working day, while others explicitly return a business day and require no date roll rule. At least one is silent on this matter.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
