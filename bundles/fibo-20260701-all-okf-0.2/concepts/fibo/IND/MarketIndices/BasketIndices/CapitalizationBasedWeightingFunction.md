---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capitalization-based weighting function
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: weighting function derived from the relative market capitalization (share price times the number of shares outstanding)
      of the companies tracked by an index
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/MarketCapitalization
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasMarketCapitalization
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/WeightingFunction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/WeightingFunction
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CapitalizationBasedWeightingFunction
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: capitalization-based weighting function
type: Ontology Class
---

# capitalization-based weighting function

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CapitalizationBasedWeightingFunction>

## Definition

weighting function derived from the relative market capitalization (share price times the number of shares outstanding) of the companies tracked by an index

## Relationships

- **Subclass of**: [WeightingFunction](/concepts/fibo/FND/Utilities/Analytics/WeightingFunction.md)

## Constraints

- **[hasMarketCapitalization](/concepts/fibo/IND/MarketIndices/BasketIndices/hasMarketCapitalization.md)**: some values from of type [MarketCapitalization](/concepts/fibo/IND/MarketIndices/BasketIndices/MarketCapitalization.md)

## Annotations

- **label** (en): capitalization-based weighting function
- **definition** (en): weighting function derived from the relative market capitalization (share price times the number of shares outstanding) of the companies tracked by an index

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
