---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business day convention
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: convention that enumerates the possible ways to handle a date that falls on a weekend or holiday
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.actusfrf.org/dictionary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Business day conventions are linked to a calendar. Calendars have working and non-working days. In the ACTUS dictionary,
      the rules related to business day conventions (BDCs) state that a BDC value other than N means that cash flows cannot
      fall on non-working days, they must be shifted to the next business day (following) or the previous on (preceding).
      These two simple rules get refined twofold: (1) Following modified (preceding): Same like following (preceding), however
      if a cash flow gets shifted into a new month, then it is shifted to preceding (following) business day; (2) Shift/calculate
      (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by this choice. In the
      case of SC first the dates are shifted and after the shift cash flows are calculated. In the case of CS it is the other
      way round.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Business day conventions commonly include:

      - Following business day: Moves the date to the next business day

      - Modified following business day: Moves the date to the next business day, unless it would fall in the next calendar
      month

      - Preceding business day: Moves the date to the previous business day

      - Modified preceding business day: Moves the date to the previous business day, unless it would fall in the previous
      calendar month'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The 2006 IDSA Definitions Section 4.11, provide the following examples: FRN Convention; Eurodollar Convention.

      - If a payment date or period end date falls on a non-business day, it is moved to the next business day.

      - If there is no numerically corresponding day in a calendar month, the payment date or period end date is moved to
      the last business day in that month.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: business day adjustment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/BusinessCenter
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasBusinessCenter
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
title: business day convention
type: Ontology Class
---

# business day convention

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention>

## Definition

convention that enumerates the possible ways to handle a date that falls on a weekend or holiday

## Relationships

- **Subclass of**: [BusinessRecurrenceIntervalConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessRecurrenceIntervalConvention.md)

## Constraints

- **[hasBusinessCenter](<https://www.omg.org/spec/Commons/Locations/hasBusinessCenter>)**: min qualified cardinality 0 of type [BusinessCenter](<https://www.omg.org/spec/Commons/Locations/BusinessCenter>)

## Annotations

- **label**: business day convention
- **definition**: convention that enumerates the possible ways to handle a date that falls on a weekend or holiday
- **adaptedFrom**: https://www.actusfrf.org/dictionary
- **explanatoryNote**: Business day conventions are linked to a calendar. Calendars have working and non-working days. In the ACTUS dictionary, the rules related to business day conventions (BDCs) state that a BDC value other than N means that cash flows cannot fall on non-working days, they must be shifted to the next business day (following) or the previous on (preceding). These two simple rules get refined twofold: (1) Following modified (preceding): Same like following (preceding), however if a cash flow gets shifted into a new month, then it is shifted to preceding (following) business day; (2) Shift/calculate (SC) and calculate/shift (CS). Accrual, principal, and possibly other calculations are affected by this choice. In the case of SC first the dates are shifted and after the shift cash flows are calculated. In the case of CS it is the other way round.
- **explanatoryNote**: Business day conventions commonly include: - Following business day: Moves the date to the next business day - Modified following business day: Moves the date to the next business day, unless it would fall in the next calendar month - Preceding business day: Moves the date to the previous business day - Modified preceding business day: Moves the date to the previous business day, unless it would fall in the previous calendar month
- **explanatoryNote**: The 2006 IDSA Definitions Section 4.11, provide the following examples: FRN Convention; Eurodollar Convention. - If a payment date or period end date falls on a non-business day, it is moved to the next business day. - If there is no numerically corresponding day in a calendar month, the payment date or period end date is moved to the last business day in that month.
- **synonym**: business day adjustment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
