---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade lifecycle event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: kind of event that occurs during one or more stages of the lifecycle of a trade
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/succeeds
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade lifecycle event
type: Ontology Class
---

# trade lifecycle event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent>

## Definition

kind of event that occurs during one or more stages of the lifecycle of a trade

## Relationships

- **Subclass of**: [LifecycleEvent](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEvent.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: min qualified cardinality 0 of type [TradeLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [TradeLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- **[succeeds](<https://www.omg.org/spec/Commons/DatesAndTimes/succeeds>)**: min qualified cardinality 0 of type [TradeLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEvent.md)

## Annotations

- **label**: trade lifecycle event
- **definition**: kind of event that occurs during one or more stages of the lifecycle of a trade

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
