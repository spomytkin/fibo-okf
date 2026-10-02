---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial product catalog
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: catalog of financial products and/or services available for sale with their description and other product details
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Nordea Bank
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/describes
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProductCatalog
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: financial product catalog
type: Ontology Class
---

# financial product catalog

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProductCatalog>

## Definition

catalog of financial products and/or services available for sale with their description and other product details

## Relationships

- **Subclass of**: [Catalog](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog.md)

## Constraints

- **[describes](<https://www.omg.org/spec/Commons/Designators/describes>)**: some values from of type [FinancialProduct](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)

## Annotations

- **label**: financial product catalog
- **definition**: catalog of financial products and/or services available for sale with their description and other product details
- **adaptedFrom**: Nordea Bank

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
