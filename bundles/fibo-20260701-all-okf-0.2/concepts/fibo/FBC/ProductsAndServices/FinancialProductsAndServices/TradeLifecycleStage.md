---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade lifecycle stage
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: phase in the lifecycle of a trade
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/succeeds
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStage
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade lifecycle stage
type: Ontology Class
---

# trade lifecycle stage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage>

## Definition

phase in the lifecycle of a trade

## Relationships

- **Subclass of**: [LifecycleStage](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStage.md)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [TradeLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Trade](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [TradeLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent.md)
- **[succeeds](<https://www.omg.org/spec/Commons/DatesAndTimes/succeeds>)**: min qualified cardinality 0 of type [TradeLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [TradeLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)

## Annotations

- **label**: trade lifecycle stage
- **definition**: phase in the lifecycle of a trade

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
