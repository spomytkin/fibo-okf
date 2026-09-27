---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade lifecycle occurrence
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: realization of the lifecycle for a specific trade
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleOccurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleOccurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade lifecycle occurrence
type: Ontology Class
---

# trade lifecycle occurrence

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleOccurrence>

## Definition

realization of the lifecycle for a specific trade

## Relationships

- **Subclass of**: [LifecycleOccurrence](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleOccurrence.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [TradeLifecycleStageOccurrence](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStageOccurrence.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: exact qualified cardinality 1 of type [TradeLifecycle](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle.md)

## Annotations

- **label**: trade lifecycle occurrence
- **definition**: realization of the lifecycle for a specific trade

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
