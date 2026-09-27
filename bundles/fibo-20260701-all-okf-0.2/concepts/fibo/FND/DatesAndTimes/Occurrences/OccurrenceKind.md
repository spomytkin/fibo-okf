---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: occurrence kind
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier that specifies the general nature of an occurrence (event)
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: loan origination
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: trade settlement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As types (or categories) of events, OccurenceKinds do not happen; OccurenceKinds describe Occurrences which happen
      and exemplify an OccurenceKind. As occurrences are things that actually happen, they have an actual date where as OccurenceKinds
      do not have an actual date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: In order for other ontologies to accept FinancialDates without committing to the particular notions of 'Occurrence'
      and 'OccurrenceKind' that is modeled here, all aspects of Occurrences are captured in this ontolog
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
sources:
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: occurrence kind
type: Ontology Class
---

# occurrence kind

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind>

## Definition

classifier that specifies the general nature of an occurrence (event)

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Annotations

- **label**: occurrence kind
- **definition**: classifier that specifies the general nature of an occurrence (event)
- **example**: loan origination
- **example**: trade settlement
- **explanatoryNote**: As types (or categories) of events, OccurenceKinds do not happen; OccurenceKinds describe Occurrences which happen and exemplify an OccurenceKind. As occurrences are things that actually happen, they have an actual date where as OccurenceKinds do not have an actual date.
- **usageNote**: In order for other ontologies to accept FinancialDates without committing to the particular notions of 'Occurrence' and 'OccurrenceKind' that is modeled here, all aspects of Occurrences are captured in this ontolog

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
