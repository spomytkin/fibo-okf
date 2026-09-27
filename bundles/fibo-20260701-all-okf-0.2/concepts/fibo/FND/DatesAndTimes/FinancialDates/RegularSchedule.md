---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regular schedule
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: schedule whose time intervals recur regularly
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: The BusinessDates ontology extends 'RegularSchedule' with an optional BusinessDayAdjustment that specifies what
      should happen if a scheduled date falls on a weekend or a holiday.
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'A 30 year mortgage is payable monthly on the 10th of the month, starting July 2015. The mortgage is issued on
      June 15, 2015 so the first payment is for the period June 15-June 30, and the last payment is for June 1-14 2045.


      The payment schedule is a RegularSchedule with these properties:


      * comprises: regular payment OccurrenceKind (with payment details) (see the ''comprises'' property of the Occurrences
      ontology)

      * hasInitialStub: June 15-30, 2015 for initial payment

      * hasFinalStub: June 1-14, 2045 for final payment

      * hasCount: 358

      * hasOverallPeriod starting Date: June 15, 2015 with a duration of 30 years

      * hasRecurrenceInterval: specifies 10th day of each calendar month

      * hasRecurrenceStartDate: July 1, 2015'
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'A corporate bond pays interest for 10 years starting on the first day of 2015. Interest payments are due 15 days
      after the expiration of each 6 month period: on July 15 and January 16.


      The payment schedule is a RegularSchedule, with these properties:


      * comprises: identifies the interest payment details

      * overall DatePeriod starting date is ''2015-01-01'', ending date is ''2025-01-15'', and duration is ''P10Y15D''

      * hasCount is 20 (2 payments per year for 10 years)

      * hasRecurrenceInterval is ''P6M''

      * hasRecurrenceStartDate is ''2015-01-15'''
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'An ISDA FpML schedule has a specified date (via a convention), and a date roll rule which is specified for the
      whole schedule and applies to each of the dates returned by the parametric specification of the schedule. It has: (1)
      a schedule beginning and end; (2) a set of regular repeating periods: the scheduled event takes place once per period;
      (3) optionally one or two stubs (one start and one end), which may be longer than the repeating period, or shorter.
      The precise parameters used are: Start of the overall Schedule period: Effective Date End of the overall Schedule period:
      Termination Date Start of first regular period: not specified (assume Effective Date) Length of each regular period:
      Frequency (a duration) There are generally three ways in which the regular periods of a parametric schedule may be expressed:
      first plus last first plus period length last plus period length event date plus period length. In FpML, Roll events
      (the date that something rolls over from the value used in one period to the value used in the next) is defined in a
      Roll Convention, which may be a day of the month, a day of the week, or some published set of dates, typically the ISDA
      quarterly dates for these events. This is therefore the date within the regular period (before adjustments) when the
      event occurs. This is in addition to a date for the start or end of such a period. In general this applies to the Calculation
      Schedule (i.e. the event is the calculation event) with other dates specified relative to this, however in principle
      the other related events (payment and reset or refix) are specified relative to this.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A RegularSchedule is a Schedule defined as a set of Dates that start on a recurrence start date and repeat after
      each recurrence interval. The size of this set is defined by a count.


      The ''initial ScheduleStub'' associated with a RegularSchedule identifies any special treatment applied before the recurrence
      start date. Similarly, a ''final ScheduleStub'' identifies any special handling at the end of the recurrences. For example,
      a mortgage loan that is due each calendar month may have an initial payment due before the first calendar month, or
      a final payment due after the last monthly payment.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A parametric schedule is a regular schedule for one of the events that occur in a periodic schedule of interest
      accruals, interest payments, and (for floating rate swapstreams), changes to the interest rate. Parametric schedules
      may be specified individually but more commonly, calculation events are scheduled, with other dates specified as offsets.
      In a regular schedule, related dates may be independently parametrically scheduled.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: parametric schedule
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: 'Other ontologies can extend RegularSchedule as needed.


      In particular, the Occurrences ontology extends RegularSchedule to ''comprise'' an ''OccurrenceKind''. The intended
      meaning is that a regular schedule comprises a number of scheduled dates and an event which is scheduled to occur on
      each of those dates, in other words an Occurrence of the OccurrenceKind should happen on each Date defined by the RegularSchedule.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: 'The recurrence start date can be an ExplicitDate or any kind of CalculatedDate. Hence, the starting date could
      be relative to another Date (e.g. T+3) or triggered by the Occurrence of an OccurrenceKind, etc.


      The recurrence start date can also be relative to the starting Date of the overall DatePeriod of the Schedule.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/BusinessDayConvention
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AnchorDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAnchorDate
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#positiveInteger
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasCount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ScheduleStub
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasFinalStub
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ScheduleStub
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasInitialStub
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate
    value: N002842143fae4d5aa6e32a3416f72e41
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/Schedule
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/StructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RegularSchedule
sources:
- id: fibo-source-7e287b0092
  resource: references/fibo/FND/DatesAndTimes/BusinessDates.rdf
  sha256: 7e287b0092247d35e3e8e12b9c1c29cba3b2b4f94d06a6b0c06e85f6c1cc2f62
  title: FIBO source FND/DatesAndTimes/BusinessDates.rdf
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
- id: fibo-source-65cb5c281b
  resource: references/fibo/SEC/Securities/ParametricSchedules.rdf
  sha256: 65cb5c281b45137091b6ba56c7877ca9362f110f63fe1d5aec4298e6583068ba
  title: FIBO source SEC/Securities/ParametricSchedules.rdf
title: regular schedule
type: Ontology Class
---

# regular schedule

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RegularSchedule>

## Definition

schedule whose time intervals recur regularly

## Relationships

- **Subclass of**: [Schedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/Schedule.md)
- **Subclass of**: [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)

## Constraints

- **[hasBusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention.md)**: max qualified cardinality 1 of type [BusinessDayConvention](/concepts/fibo/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md)
- **[hasAnchorDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAnchorDate.md)**: min qualified cardinality 0 of type [AnchorDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/AnchorDate.md)
- **[hasCount](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasCount.md)**: exact qualified cardinality 1 of type [positiveInteger](<http://www.w3.org/2001/XMLSchema#positiveInteger>)
- **[hasFinalStub](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasFinalStub.md)**: min qualified cardinality 0 of type [ScheduleStub](/concepts/fibo/FND/DatesAndTimes/FinancialDates/ScheduleStub.md)
- **[hasInitialStub](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasInitialStub.md)**: min qualified cardinality 0 of type [ScheduleStub](/concepts/fibo/FND/DatesAndTimes/FinancialDates/ScheduleStub.md)
- **[hasRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasRecurrenceInterval.md)**: some values from of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: min qualified cardinality 0 of type [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- **[hasStartDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasStartDate>)**: some values from value `N002842143fae4d5aa6e32a3416f72e41`

## Annotations

- **label**: regular schedule
- **definition**: schedule whose time intervals recur regularly
- **editorialNote**: The BusinessDates ontology extends 'RegularSchedule' with an optional BusinessDayAdjustment that specifies what should happen if a scheduled date falls on a weekend or a holiday.
- **example**: A 30 year mortgage is payable monthly on the 10th of the month, starting July 2015. The mortgage is issued on June 15, 2015 so the first payment is for the period June 15-June 30, and the last payment is for June 1-14 2045.  The payment schedule is a RegularSchedule with these properties:  * comprises: regular payment OccurrenceKind (with payment details) (see the 'comprises' property of the Occurrences ontology) * hasInitialStub: June 15-30, 2015 for initial payment * hasFinalStub: June 1-14, 2045 for final payment * hasCount: 358 * hasOverallPeriod starting Date: June 15, 2015 with a duration of 30 years * hasRecurrenceInterval: specifies 10th day of each calendar month * hasRecurrenceStartDate: July 1, 2015
- **example**: A corporate bond pays interest for 10 years starting on the first day of 2015. Interest payments are due 15 days after the expiration of each 6 month period: on July 15 and January 16.  The payment schedule is a RegularSchedule, with these properties:  * comprises: identifies the interest payment details * overall DatePeriod starting date is '2015-01-01', ending date is '2025-01-15', and duration is 'P10Y15D' * hasCount is 20 (2 payments per year for 10 years) * hasRecurrenceInterval is 'P6M' * hasRecurrenceStartDate is '2015-01-15'
- **example**: An ISDA FpML schedule has a specified date (via a convention), and a date roll rule which is specified for the whole schedule and applies to each of the dates returned by the parametric specification of the schedule. It has: (1) a schedule beginning and end; (2) a set of regular repeating periods: the scheduled event takes place once per period; (3) optionally one or two stubs (one start and one end), which may be longer than the repeating period, or shorter. The precise parameters used are: Start of the overall Schedule period: Effective Date End of the overall Schedule period: Termination Date Start of first regular period: not specified (assume Effective Date) Length of each regular period: Frequency (a duration) There are generally three ways in which the regular periods of a parametric schedule may be expressed: first plus last first plus period length last plus period length event date plus period length. In FpML, Roll events (the date that something rolls over from the value used in one period to the value used in the next) is defined in a Roll Convention, which may be a day of the month, a day of the week, or some published set of dates, typically the ISDA quarterly dates for these events. This is therefore the date within the regular period (before adjustments) when the event occurs. This is in addition to a date for the start or end of such a period. In general this applies to the Calculation Schedule (i.e. the event is the calculation event) with other dates specified relative to this, however in principle the other related events (payment and reset or refix) are specified relative to this.
- **explanatoryNote**: A RegularSchedule is a Schedule defined as a set of Dates that start on a recurrence start date and repeat after each recurrence interval. The size of this set is defined by a count.  The 'initial ScheduleStub' associated with a RegularSchedule identifies any special treatment applied before the recurrence start date. Similarly, a 'final ScheduleStub' identifies any special handling at the end of the recurrences. For example, a mortgage loan that is due each calendar month may have an initial payment due before the first calendar month, or a final payment due after the last monthly payment.
- **explanatoryNote**: A parametric schedule is a regular schedule for one of the events that occur in a periodic schedule of interest accruals, interest payments, and (for floating rate swapstreams), changes to the interest rate. Parametric schedules may be specified individually but more commonly, calculation events are scheduled, with other dates specified as offsets. In a regular schedule, related dates may be independently parametrically scheduled.
- **synonym**: parametric schedule
- **usageNote**: Other ontologies can extend RegularSchedule as needed.  In particular, the Occurrences ontology extends RegularSchedule to 'comprise' an 'OccurrenceKind'. The intended meaning is that a regular schedule comprises a number of scheduled dates and an event which is scheduled to occur on each of those dates, in other words an Occurrence of the OccurrenceKind should happen on each Date defined by the RegularSchedule.
- **usageNote**: The recurrence start date can be an ExplicitDate or any kind of CalculatedDate. Hence, the starting date could be relative to another Date (e.g. T+3) or triggered by the Occurrence of an OccurrenceKind, etc.  The recurrence start date can also be relative to the starting Date of the overall DatePeriod of the Schedule.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
