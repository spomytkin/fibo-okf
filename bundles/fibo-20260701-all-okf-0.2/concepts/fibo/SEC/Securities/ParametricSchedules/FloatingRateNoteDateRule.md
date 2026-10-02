---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: floating-rate note date rule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: business day adjustment rule applied to floating-rate note instruments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FRN date rule
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/FloatingRateNoteDateRule
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: floating-rate note date rule
type: Ontology Class
---

# floating-rate note date rule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/FloatingRateNoteDateRule>

## Definition

business day adjustment rule applied to floating-rate note instruments

## Relationships

- **Subclass of**: [BusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)

## Annotations

- **label**: floating-rate note date rule
- **definition**: business day adjustment rule applied to floating-rate note instruments
- **abbreviation**: FRN date rule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
