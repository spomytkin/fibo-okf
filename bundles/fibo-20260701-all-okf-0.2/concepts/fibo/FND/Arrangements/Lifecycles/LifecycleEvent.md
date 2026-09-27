---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lifecycle event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: kind of event that occurs during one or more stages of a lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: a call notification or coupon payment as a part of a bond lifecycle
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEvent
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: lifecycle event
type: Ontology Class
---

# lifecycle event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEvent>

## Definition

kind of event that occurs during one or more stages of a lifecycle

## Relationships

- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)

## Annotations

- **label**: lifecycle event
- **definition**: kind of event that occurs during one or more stages of a lifecycle
- **example**: a call notification or coupon payment as a part of a bond lifecycle

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
