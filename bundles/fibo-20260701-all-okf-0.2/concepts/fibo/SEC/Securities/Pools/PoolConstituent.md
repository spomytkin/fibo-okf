---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pool constituent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: component of a pool
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A pool may consist of almost anything brought together for some purpose. It differs from a less formal collection
      in that there are typically facts defined about the members of the pool and potentially regarding the proportions of
      those members in the pool. Pool membership may change over time, and certain facts about the pool may also vary over
      time. However, the basic nature of something as a member of the pool is static while that membership holds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Constituent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PoolConstituent
sources:
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: pool constituent
type: Ontology Class
---

# pool constituent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PoolConstituent>

## Definition

component of a pool

## Relationships

- **Subclass of**: [Constituent](<https://www.omg.org/spec/Commons/Collections/Constituent>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: some values from of type [Pool](/concepts/fibo/SEC/Securities/Pools/Pool.md)

## Annotations

- **label**: pool constituent
- **definition**: component of a pool
- **explanatoryNote**: A pool may consist of almost anything brought together for some purpose. It differs from a less formal collection in that there are typically facts defined about the members of the pool and potentially regarding the proportions of those members in the pool. Pool membership may change over time, and certain facts about the pool may also vary over time. However, the basic nature of something as a member of the pool is static while that membership holds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
