---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has generating entity identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies an identifier for the entity that generated a unique transaction identifier
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the range of is identified by must be that entity's LEI in the context of a UTI.
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/UniqueTransactionIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/UniqueTransactionIdentifier
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasGeneratingEntityIdentifier
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: has generating entity identifier
type: Ontology Property
---

# has generating entity identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasGeneratingEntityIdentifier>

## Definition

specifies an identifier for the entity that generated a unique transaction identifier

## Relationships

- **Domain**: [UniqueTransactionIdentifier](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/UniqueTransactionIdentifier.md)

## Annotations

- **label**: has generating entity identifier
- **definition**: specifies an identifier for the entity that generated a unique transaction identifier
- **explanatoryNote**: Note that the range of is identified by must be that entity's LEI in the context of a UTI.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
