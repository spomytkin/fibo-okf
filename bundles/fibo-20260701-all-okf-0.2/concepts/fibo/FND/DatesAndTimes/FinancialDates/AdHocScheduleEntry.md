---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ad hoc schedule entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry, including a date or date and time, among multiple non-regularly-recurring entries in a schedule
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Other ontologies can extend AdHocScheduleEntry as needed. In particular, the Occurrences ontology extends AdHocScheduleEntry
      to consist of occurrences (events) of a given OccurrenceKind. The meaning is that an ad hoc schedule entry comprises
      a date and an event which is scheduled to occur on that date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: 'The Date of an AdHocScheduleEntry can be an ExplicitDate or any kind of CalculatedDate, such as:


      * An OccurrenceBasedDate -- a Date that itself is defined by an Occurrence (see the Occurrences ontology)

      * A RelativeDate - a Date relative to another Date, such as T+3

      * A SpecifiedDate - a Date that is defined by an arbitrary rule'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: The cmns-dt;hasDate property may be used to reify a date, if it is important to do so for a given application,
      or if not and typically, the inherited cmns-dt;hasObservedDateTime property may be used together with a cmns-dt;CombinedDateTime
      value, as long as the resulting schedule is consistent in using one or the other.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOccurrence
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: ad hoc schedule entry
type: Ontology Class
---

# ad hoc schedule entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry>

## Definition

entry, including a date or date and time, among multiple non-regularly-recurring entries in a schedule

## Relationships

- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)

## Constraints

- **[hasOccurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOccurrence.md)**: min qualified cardinality 0 of type [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Annotations

- **label**: ad hoc schedule entry
- **definition**: entry, including a date or date and time, among multiple non-regularly-recurring entries in a schedule
- **usageNote**: Other ontologies can extend AdHocScheduleEntry as needed. In particular, the Occurrences ontology extends AdHocScheduleEntry to consist of occurrences (events) of a given OccurrenceKind. The meaning is that an ad hoc schedule entry comprises a date and an event which is scheduled to occur on that date.
- **usageNote**: The Date of an AdHocScheduleEntry can be an ExplicitDate or any kind of CalculatedDate, such as:  * An OccurrenceBasedDate -- a Date that itself is defined by an Occurrence (see the Occurrences ontology) * A RelativeDate - a Date relative to another Date, such as T+3 * A SpecifiedDate - a Date that is defined by an arbitrary rule
- **usageNote**: The cmns-dt;hasDate property may be used to reify a date, if it is important to do so for a given application, or if not and typically, the inherited cmns-dt;hasObservedDateTime property may be used together with a cmns-dt;CombinedDateTime value, as long as the resulting schedule is consistent in using one or the other.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
