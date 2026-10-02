---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: occurrence-based date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: calculated date that is defined with respect to the occurrence of some occurrence kind
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The 'hasDateValue' property of an OccurrenceBasedDate is not set until the Occurrence happens. The 'triggeredBy'
      property relates an OccurrenceBasedDate to the OccurrenceKind that gives the meaning of the OccurrenceBasedDate.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/isTriggeredBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/CalculatedDate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate
sources:
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: occurrence-based date
type: Ontology Class
---

# occurrence-based date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate>

## Definition

calculated date that is defined with respect to the occurrence of some occurrence kind

## Relationships

- **Subclass of**: [CalculatedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)

## Constraints

- **[isTriggeredBy](/concepts/fibo/FND/DatesAndTimes/Occurrences/isTriggeredBy.md)**: exact qualified cardinality 1 of type [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Annotations

- **label**: occurrence-based date
- **definition**: calculated date that is defined with respect to the occurrence of some occurrence kind
- **explanatoryNote**: The 'hasDateValue' property of an OccurrenceBasedDate is not set until the Occurrence happens. The 'triggeredBy' property relates an OccurrenceBasedDate to the OccurrenceKind that gives the meaning of the OccurrenceBasedDate.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
