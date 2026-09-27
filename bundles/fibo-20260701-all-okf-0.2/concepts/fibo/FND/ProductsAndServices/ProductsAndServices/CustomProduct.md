---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: custom product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: product that is made to order, commissioned based on a customer's specifications
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bespoke product
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: custom-made product
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: made to order product
  disjoint_with:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/CustomProduct
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: custom product
type: Ontology Class
---

# custom product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/CustomProduct>

## Definition

product that is made to order, commissioned based on a customer's specifications

## Relationships

- **Subclass of**: [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)

## Constraints

- **Disjoint with**: [OffTheShelfProduct](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/OffTheShelfProduct.md)

## Annotations

- **label**: custom product
- **definition**: product that is made to order, commissioned based on a customer's specifications
- **synonym**: bespoke product
- **synonym**: custom-made product
- **synonym**: made to order product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
