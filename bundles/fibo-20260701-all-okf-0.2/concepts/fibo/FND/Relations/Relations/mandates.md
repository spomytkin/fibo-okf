---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mandates
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something to a commitment, contract, law, obligation, requirement, regulation, or similar concept that
      requires it
  inverse_of:
  - concept: /concepts/fibo/FND/Relations/Relations/isMandatedBy.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/confers.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/mandates
sources:
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: mandates
type: Ontology Property
---

# mandates

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/mandates>

## Definition

relates something to a commitment, contract, law, obligation, requirement, regulation, or similar concept that requires it

## Relationships

- **Inverse of**: [isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)
- **Subproperty of**: [confers](/concepts/fibo/FND/Relations/Relations/confers.md)

## Annotations

- **label**: mandates
- **definition**: relates something to a commitment, contract, law, obligation, requirement, regulation, or similar concept that requires it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
