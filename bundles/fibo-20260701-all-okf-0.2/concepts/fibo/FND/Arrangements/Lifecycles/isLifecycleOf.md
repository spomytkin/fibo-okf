---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is lifecycle of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a lifecycle to something it characterizes
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
  inverse_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/hasLifecycle.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasLifecycle
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/characterizes
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isLifecycleOf
sources:
- id: fibo-source-92efc72f29
  resource: references/fibo/FND/Arrangements/Lifecycles.rdf
  sha256: 92efc72f29aba7c64208722174530078a5a46ad575d7ceabbf0cd9a444ad5e0e
  title: FIBO source FND/Arrangements/Lifecycles.rdf
title: is lifecycle of
type: Ontology Property
---

# is lifecycle of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isLifecycleOf>

## Definition

relates a lifecycle to something it characterizes

## Relationships

- **Domain**: [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)
- **Inverse of**: [hasLifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/hasLifecycle.md)
- **Subproperty of**: [characterizes](<https://www.omg.org/spec/Commons/Classifiers/characterizes>)

## Annotations

- **label**: is lifecycle of
- **definition**: relates a lifecycle to something it characterizes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
