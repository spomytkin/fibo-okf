---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection of events, observations, or other occurrences and the associated dates and/or times when they will be
      done
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The overall period covers the entire DatePeriod of the Schedule, from the earliest Date to the final Date of the
      Schedule. Schedules may be ad hoc, essentially a list of dates and events without any consistency in the durations between
      events, regular, in which case there is a consistently recurring interval between events, or a combination of the two.
      There may be a single overall period, or more than one if the schedule is extended for some reason.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOverallPeriod
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: schedule
type: Ontology Class
---

# schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule>

## Definition

collection of events, observations, or other occurrences and the associated dates and/or times when they will be done

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasOverallPeriod](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasOverallPeriod.md)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: schedule
- **definition**: collection of events, observations, or other occurrences and the associated dates and/or times when they will be done
- **explanatoryNote**: The overall period covers the entire DatePeriod of the Schedule, from the earliest Date to the final Date of the Schedule. Schedules may be ad hoc, essentially a list of dates and events without any consistency in the durations between events, regular, in which case there is a consistently recurring interval between events, or a combination of the two. There may be a single overall period, or more than one if the schedule is extended for some reason.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
