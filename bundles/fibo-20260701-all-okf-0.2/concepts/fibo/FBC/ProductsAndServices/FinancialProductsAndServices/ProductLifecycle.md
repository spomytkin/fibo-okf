---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: product lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lifecycle specific to a product or product family
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'The product life cycle describes the period of time over which an item is developed, brought to market and eventually
      removed from the market. The cycle is broken into four stages: introduction, growth, maturity and decline. The idea
      of the product life cycle is used in marketing to decide when it is appropriate to advertise, reduce prices, explore
      new markets or create new packaging.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isLifecycleOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: product lifecycle
type: Ontology Class
---

# product lifecycle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle>

## Definition

lifecycle specific to a product or product family

## Relationships

- **Subclass of**: [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [ProductLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)
- **[isLifecycleOf](/concepts/fibo/FND/Arrangements/Lifecycles/isLifecycleOf.md)**: some values from of type [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [ProductLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)

## Annotations

- **label**: product lifecycle
- **definition**: lifecycle specific to a product or product family
- **example**: The product life cycle describes the period of time over which an item is developed, brought to market and eventually removed from the market. The cycle is broken into four stages: introduction, growth, maturity and decline. The idea of the product life cycle is used in marketing to decide when it is appropriate to advertise, reduce prices, explore new markets or create new packaging.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
