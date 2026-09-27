---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has generating entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a legal entity that generates something
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/generates.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/generates
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasGeneratingEntity
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has generating entity
type: Ontology Property
---

# has generating entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasGeneratingEntity>

## Definition

specifies a legal entity that generates something

## Relationships

- **Range**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Subproperty of**: [generates](/concepts/fibo/FND/Relations/Relations/generates.md)

## Annotations

- **label**: has generating entity
- **definition**: specifies a legal entity that generates something

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
