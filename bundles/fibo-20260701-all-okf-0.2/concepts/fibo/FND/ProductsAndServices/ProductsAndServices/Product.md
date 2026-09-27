---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commercially distributed good that is (1) tangible property, (2) the output or result of a fabrication, manufacturing,
      or production process, or (3) something that passes through a distribution channel before being consumed or used.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Financial products include contracts that are developed via a financial service-specific process, such as a life
      insurance policy, demand deposit account or financial instrument, for example. Leases and rentals are similar in that
      they are initiated via some contractual development process, wherein the product is the right to use something for some
      period of time.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasLifecycle
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: product
type: Ontology Class
---

# product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product>

## Definition

commercially distributed good that is (1) tangible property, (2) the output or result of a fabrication, manufacturing, or production process, or (3) something that passes through a distribution channel before being consumed or used.

## Constraints

- **[hasLifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/hasLifecycle.md)**: min qualified cardinality 0 of type [ProductLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: min qualified cardinality 0 of type [Catalog](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Catalog.md)

## Annotations

- **label**: product
- **definition**: commercially distributed good that is (1) tangible property, (2) the output or result of a fabrication, manufacturing, or production process, or (3) something that passes through a distribution channel before being consumed or used.
- **explanatoryNote**: Financial products include contracts that are developed via a financial service-specific process, such as a life insurance policy, demand deposit account or financial instrument, for example. Leases and rentals are similar in that they are initiated via some contractual development process, wherein the product is the right to use something for some period of time.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
