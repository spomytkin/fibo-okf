---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dated collection constituent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: element of a collection that is associated with a date and time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the use of several options for the representation of a date and time stamp enables extensions for milliseconds,
      nanoseconds using an xsd:string that has the format of an xsd:dateTime datatype but extends the level of granularity
      consistently. An example of where this is required is to represent prices that change multiple times in a given day.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: The use of custom datatypes is outside the OWL 2 RL profile and so users should consider commenting out the restriction
      on hasObservedDateTime altogether or change the data range to rdfs:Literal in applications that are constrained to OWL
      2 RL.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Constituent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: dated collection constituent
type: Ontology Class
---

# dated collection constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent>

## Definition

element of a collection that is associated with a date and time

## Relationships

- **Subclass of**: [Constituent](<https://www.omg.org/spec/Commons/Collections/Constituent>)

## Constraints

- **[hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)**: some values from of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: dated collection constituent
- **definition**: element of a collection that is associated with a date and time
- **explanatoryNote**: Note that the use of several options for the representation of a date and time stamp enables extensions for milliseconds, nanoseconds using an xsd:string that has the format of an xsd:dateTime datatype but extends the level of granularity consistently. An example of where this is required is to represent prices that change multiple times in a given day.
- **usageNote**: The use of custom datatypes is outside the OWL 2 RL profile and so users should consider commenting out the restriction on hasObservedDateTime altogether or change the data range to rdfs:Literal in applications that are constrained to OWL 2 RL.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
