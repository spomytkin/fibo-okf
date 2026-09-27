---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: scheduled calculation period start event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the start of a specific calculation period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: FpML for CalculationPeriod 'A type defining the parameters used in the calculation of a fixed or floating rate
      calculation period amount. This type forms part of cashflows representation of a swap stream.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/ScheduledCalculationPeriodStartEvent
sources:
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: scheduled calculation period start event
type: Ontology Class
---

# scheduled calculation period start event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/ScheduledCalculationPeriodStartEvent>

## Definition

the start of a specific calculation period

## Relationships

- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Annotations

- **label**: scheduled calculation period start event
- **definition**: the start of a specific calculation period
- **explanatoryNote**: FpML for CalculationPeriod 'A type defining the parameters used in the calculation of a fixed or floating rate calculation period amount. This type forms part of cashflows representation of a swap stream.'

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
