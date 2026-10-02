---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calendar period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: time interval that occurs within a system that fixes the beginning and length of a segment of the year with respect
      to that system
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: "The terms 'calendar xxx' are intended to reinforce that these are periods on a calendar, not durations. \n\nFor\
      \ example, a calendar year always starts on a January 1 and ends on a December 31. The term 'calendar year' does not\
      \ mean the same thing as a duration (an amount of time) of 1 year, nor can a calendar year start on any arbitrary day\
      \ of a year. For example, a calendar year never starts on September 1.\n\nSimilar points apply to other kinds of calendar\
      \ periods, such as calendar week, calendar month, and calendar quarter."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A calendar-specified date may be figured with respect to a calendar week, a calendar month, a calendar quarter,
      or a calendar year.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/TimeInterval
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalendarPeriod
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: calendar period
type: Ontology Class
---

# calendar period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalendarPeriod>

## Definition

time interval that occurs within a system that fixes the beginning and length of a segment of the year with respect to that system

## Relationships

- **Subclass of**: [TimeInterval](<https://www.omg.org/spec/Commons/DatesAndTimes/TimeInterval>)

## Annotations

- **label**: calendar period
- **definition**: time interval that occurs within a system that fixes the beginning and length of a segment of the year with respect to that system
- **editorialNote**: The terms 'calendar xxx' are intended to reinforce that these are periods on a calendar, not durations.   For example, a calendar year always starts on a January 1 and ends on a December 31. The term 'calendar year' does not mean the same thing as a duration (an amount of time) of 1 year, nor can a calendar year start on any arbitrary day of a year. For example, a calendar year never starts on September 1.  Similar points apply to other kinds of calendar periods, such as calendar week, calendar month, and calendar quarter.
- **explanatoryNote**: A calendar-specified date may be figured with respect to a calendar week, a calendar month, a calendar quarter, or a calendar year.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
