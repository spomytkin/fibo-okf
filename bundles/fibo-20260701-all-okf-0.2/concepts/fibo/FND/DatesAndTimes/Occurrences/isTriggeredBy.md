---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is triggered by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is activated or initiated by
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An OccurrenceBasedDate is triggered by an Occurrence that exemplifies the OccurrenceKind.
  domain:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/isTriggeredBy
sources:
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: is triggered by
type: Ontology Property
---

# is triggered by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/isTriggeredBy>

## Definition

is activated or initiated by

## Relationships

- **Domain**: [OccurrenceBasedDate](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceBasedDate.md)
- **Range**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Annotations

- **label**: is triggered by
- **definition**: is activated or initiated by
- **explanatoryNote**: An OccurrenceBasedDate is triggered by an Occurrence that exemplifies the OccurrenceKind.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
