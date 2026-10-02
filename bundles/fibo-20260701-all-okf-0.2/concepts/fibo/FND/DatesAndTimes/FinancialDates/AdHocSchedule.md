---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ad hoc schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule consisting of some number of individual events that are not necessarily recurring
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Other ontologies can extend AdHocSchedule and/or AdHocScheduleEntry as needed to relate the date to something.
      In particular, the Occurrences ontology extends AdHocScheduleEntry to associate an OccurrenceKind with each entry. The
      intended meaning is that an Occurrence of the OccurrenceKind happens on the corresponding Date.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocSchedule
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: ad hoc schedule
type: Ontology Class
---

# ad hoc schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocSchedule>

## Definition

schedule consisting of some number of individual events that are not necessarily recurring

## Relationships

- **Subclass of**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [AdHocScheduleEntry](/concepts/fibo/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry.md)

## Annotations

- **label**: ad hoc schedule
- **definition**: schedule consisting of some number of individual events that are not necessarily recurring
- **usageNote**: Other ontologies can extend AdHocSchedule and/or AdHocScheduleEntry as needed to relate the date to something. In particular, the Occurrences ontology extends AdHocScheduleEntry to associate an OccurrenceKind with each entry. The intended meaning is that an Occurrence of the OccurrenceKind happens on the corresponding Date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
