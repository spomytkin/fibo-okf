---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: happening of an OccurrenceKind, i.e., an event
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Each occurrence has a date time stamp, which identifies when the event occurred, and, optionally, a location (possibly
      virtual), that identifies where the occurrence happened.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: event
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: In order for other ontologies to accept FinancialDates without committing to the particular notions of 'Occurrence'
      and 'OccurrenceKind' that is modeled here, all aspects of Occurrences are captured in this ontology.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/Location
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasLocation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
sources:
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: occurrence
type: Ontology Class
---

# occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence>

## Definition

happening of an OccurrenceKind, i.e., an event

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- **[hasLocation](<https://www.omg.org/spec/Commons/Locations/hasLocation>)**: min qualified cardinality 0 of type [Location](<https://www.omg.org/spec/Commons/Locations/Location>)

## Annotations

- **label**: occurrence
- **definition**: happening of an OccurrenceKind, i.e., an event
- **explanatoryNote**: Each occurrence has a date time stamp, which identifies when the event occurred, and, optionally, a location (possibly virtual), that identifies where the occurrence happened.
- **synonym**: event
- **usageNote**: In order for other ontologies to accept FinancialDates without committing to the particular notions of 'Occurrence' and 'OccurrenceKind' that is modeled here, all aspects of Occurrences are captured in this ontology.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
