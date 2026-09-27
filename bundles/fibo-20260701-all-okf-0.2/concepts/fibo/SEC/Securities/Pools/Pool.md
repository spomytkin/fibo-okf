---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pool
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: combination of resources for a common purpose or benefit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PoolConstituent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool
sources:
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: pool
type: Ontology Class
---

# pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool>

## Definition

combination of resources for a common purpose or benefit

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [PoolConstituent](/concepts/fibo/SEC/Securities/Pools/PoolConstituent.md)

## Annotations

- **label**: pool
- **definition**: combination of resources for a common purpose or benefit
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
