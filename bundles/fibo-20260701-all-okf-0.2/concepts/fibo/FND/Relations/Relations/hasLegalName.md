---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has legal name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the name used to refer to a party in legal communications
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/hasFormalName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
sources:
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: has legal name
type: Ontology Property
---

# has legal name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName>

## Definition

specifies the name used to refer to a party in legal communications

## Relationships

- **Subproperty of**: [hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)

## Annotations

- **label**: has legal name
- **definition**: specifies the name used to refer to a party in legal communications

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
