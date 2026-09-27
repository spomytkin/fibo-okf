---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: product lifecycle stage
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: phase in a product lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: research and development phase of a product lifecycle or the introduction phase in a marketing lifecycle, growth
      stage in an economic lifecycle for a product
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Product
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/succeeds
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: product lifecycle stage
type: Ontology Class
---

# product lifecycle stage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage>

## Definition

phase in a product lifecycle

## Relationships

- **Subclass of**: [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [ProductLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Product](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Product.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [ProductLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleEvent.md)
- **[succeeds](<https://www.omg.org/spec/Commons/DatesAndTimes/succeeds>)**: min qualified cardinality 0 of type [ProductLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycleStage.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [ProductLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ProductLifecycle.md)

## Annotations

- **label**: product lifecycle stage
- **definition**: phase in a product lifecycle
- **example**: research and development phase of a product lifecycle or the introduction phase in a marketing lifecycle, growth stage in an economic lifecycle for a product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
