---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade lifecycle
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lifecycle that defines the evolution of a trade, from initiation through settlement
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The trade life cycle covers the period of time over which a trade is initiated, typically as a part of a broader
      deal, is consumated, processed and executed, is settled or closed for other reasons, and is reported. Parts of a trade
      lifecycle may include or overlap with the lifecycle of one or more contracts.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Trade
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/isLifecycleOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/Lifecycle
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: trade lifecycle
type: Ontology Class
---

# trade lifecycle

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycle>

## Definition

lifecycle that defines the evolution of a trade, from initiation through settlement

## Relationships

- **Subclass of**: [Lifecycle](/concepts/fibo/FND/Arrangements/Lifecycles/Lifecycle.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [TradeLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)
- **[isLifecycleOf](/concepts/fibo/FND/Arrangements/Lifecycles/isLifecycleOf.md)**: some values from of type [Trade](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Trade.md)
- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [TradeLifecycleStage](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradeLifecycleStage.md)

## Annotations

- **label**: trade lifecycle
- **definition**: lifecycle that defines the evolution of a trade, from initiation through settlement
- **example**: The trade life cycle covers the period of time over which a trade is initiated, typically as a part of a broader deal, is consumated, processed and executed, is settled or closed for other reasons, and is reported. Parts of a trade lifecycle may include or overlap with the lifecycle of one or more contracts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
