---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something, such as a product, trade, or related process, to a lifecycle that characterizes it
  range:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasLifecycle
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: has lifecycle
type: Ontology Property
---

# has lifecycle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasLifecycle>

## Definition

relates something, such as a product, trade, or related process, to a lifecycle that characterizes it

## Relationships

- **Range**: [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)
- **Subproperty of**: [isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)

## Annotations

- **label**: has lifecycle
- **definition**: relates something, such as a product, trade, or related process, to a lifecycle that characterizes it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
