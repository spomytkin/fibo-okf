---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: schedule stub
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: date period before the start of the recurring part of a schedule or after the end of the recurring part, which
      may be associated with a specific occurrence kind
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: The Occurrences ontology extends ScheduleStub to 'comprise' an OccurrenceKind. The meaning is that a schedule stub
      comprises a date period and an event which is scheduled to occur during that date period; in other words that an Occurrence
      of the OccurrenceKind should happen during the DatePeriod of the ScheduleStub.
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: A 30 year mortgage calls for monthly payments on the first day of each month, according to a RegularSchedule. If
      the mortgage does not start on the first day of a calendar month, then an initial ScheduleStub specifies the payment
      due for the DatePeriod up to the first day of the next calendar month. Similarly, a final ScheduleStub specifies the
      last payment due for the DatePeriod after the end of the last full calendar month.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ScheduleStub
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: schedule stub
type: Ontology Class
---

# schedule stub

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ScheduleStub>

## Definition

date period before the start of the recurring part of a schedule or after the end of the recurring part, which may be associated with a specific occurrence kind

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: min qualified cardinality 0 of type [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: exact qualified cardinality 1 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: schedule stub
- **definition**: date period before the start of the recurring part of a schedule or after the end of the recurring part, which may be associated with a specific occurrence kind
- **editorialNote**: The Occurrences ontology extends ScheduleStub to 'comprise' an OccurrenceKind. The meaning is that a schedule stub comprises a date period and an event which is scheduled to occur during that date period; in other words that an Occurrence of the OccurrenceKind should happen during the DatePeriod of the ScheduleStub.
- **example**: A 30 year mortgage calls for monthly payments on the first day of each month, according to a RegularSchedule. If the mortgage does not start on the first day of a calendar month, then an initial ScheduleStub specifies the payment due for the DatePeriod up to the first day of the next calendar month. Similarly, a final ScheduleStub specifies the last payment due for the DatePeriod after the end of the last full calendar month.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
