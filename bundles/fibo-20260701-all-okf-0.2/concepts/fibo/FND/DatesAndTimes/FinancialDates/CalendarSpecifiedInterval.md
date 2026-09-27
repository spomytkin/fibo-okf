---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calendar-specified interval
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: recurrence interval that is defined as the nth day of some calendar period (such as a calendar month), and a time
      direction (forward from the beginning of the month, or backwards from the end)
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The 15th day of each calendar month.
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The last day of each quarter, specified as RelativeDay 1, and TimeDirection set to FromEnd.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The nth day is an ordinal number, not a cardinal number. '1' means the first day of the calendar period.
  disjoint_with:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalendarPeriod
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasCalendarPeriod
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#integer
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOrdinalNumber
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/TimeDirection
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasTimeDirection
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalendarSpecifiedInterval
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: calendar-specified interval
type: Ontology Class
---

# calendar-specified interval

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalendarSpecifiedInterval>

## Definition

recurrence interval that is defined as the nth day of some calendar period (such as a calendar month), and a time direction (forward from the beginning of the month, or backwards from the end)

## Relationships

- **Subclass of**: [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)

## Constraints

- **Disjoint with**: [ExplicitRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md)
- **[hasCalendarPeriod](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasCalendarPeriod.md)**: exact qualified cardinality 1 of type [CalendarPeriod](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalendarPeriod.md)
- **[hasOrdinalNumber](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasOrdinalNumber.md)**: exact qualified cardinality 1 of type [integer](<http://www.w3.org/2001/XMLSchema#integer>)
- **[hasTimeDirection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasTimeDirection.md)**: exact qualified cardinality 1 of type [TimeDirection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/TimeDirection.md)

## Annotations

- **label**: calendar-specified interval
- **definition**: recurrence interval that is defined as the nth day of some calendar period (such as a calendar month), and a time direction (forward from the beginning of the month, or backwards from the end)
- **example**: The 15th day of each calendar month.
- **example**: The last day of each quarter, specified as RelativeDay 1, and TimeDirection set to FromEnd.
- **explanatoryNote**: The nth day is an ordinal number, not a cardinal number. '1' means the first day of the calendar period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
