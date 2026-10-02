---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lifecycle stage occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: realization of a phase in a given lifecycle
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleOccurrence
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEventOccurrence
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStageOccurrence
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: lifecycle stage occurrence
type: Ontology Class
---

# lifecycle stage occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStageOccurrence>

## Definition

realization of a phase in a given lifecycle

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [LifecycleOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleOccurrence.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [LifecycleEventOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEventOccurrence.md)

## Annotations

- **label**: lifecycle stage occurrence
- **definition**: realization of a phase in a given lifecycle

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
