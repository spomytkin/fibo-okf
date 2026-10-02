---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is caused by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: is the relationship between an event (the effect) and a second event (the cause), where the first event is understood
      as a consequence of the second; also, the relationship between a set of factors (causes) and a phenomenon (the effect)
  inverse_of:
  - concept: /concepts/fibo/FND/Relations/Relations/causes.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/causes
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isCausedBy
sources:
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: is caused by
type: Ontology Property
---

# is caused by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isCausedBy>

## Definition

is the relationship between an event (the effect) and a second event (the cause), where the first event is understood as a consequence of the second; also, the relationship between a set of factors (causes) and a phenomenon (the effect)

## Relationships

- **Inverse of**: [causes](/concepts/fibo/FND/Relations/Relations/causes.md)

## Annotations

- **label**: is caused by
- **definition**: is the relationship between an event (the effect) and a second event (the cause), where the first event is understood as a consequence of the second; also, the relationship between a set of factors (causes) and a phenomenon (the effect)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
