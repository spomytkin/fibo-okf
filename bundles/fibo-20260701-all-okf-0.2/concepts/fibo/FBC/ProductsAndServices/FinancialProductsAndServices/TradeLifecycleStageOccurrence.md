---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade lifecycle stage occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: realization of a phase in the lifecycle of a specific trade
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isStageOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/succeeds
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStageOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade lifecycle stage occurrence
type: Ontology Class
---

# trade lifecycle stage occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence>

## Definition

realization of a phase in the lifecycle of a specific trade

## Relationships

- **Subclass of**: [LifecycleStageOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md)

## Constraints

- **[isStageOf](/concepts/fibo/FND/Arrangements/Lifecycles/isStageOf.md)**: some values from of type [TradeLifecycleOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [TradeLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [TradeLifecycleEventOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleEventOccurrence.md)
- **[succeeds](<https://www.omg.org/spec/Commons/DatesAndTimes/succeeds>)**: min qualified cardinality 0 of type [TradeLifecycleStageOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence.md)

## Annotations

- **label**: trade lifecycle stage occurrence
- **definition**: realization of a phase in the lifecycle of a specific trade

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
