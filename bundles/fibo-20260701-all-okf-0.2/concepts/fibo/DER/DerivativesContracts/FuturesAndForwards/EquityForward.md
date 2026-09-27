---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity forward
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: forward contract to buy or sell the underlying equity stock, equity index, basket of equity stock, equity futures
      contract, or equity option at a specified future date at the price specified at the outset of the contract
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasDividendAdjustmentPeriod
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/hasMethodOfAdjustment
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N234b453206934b90a71c465bc6be0444
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/Forward.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityForward
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: equity forward
type: Ontology Class
---

# equity forward

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityForward>

## Definition

forward contract to buy or sell the underlying equity stock, equity index, basket of equity stock, equity futures contract, or equity option at a specified future date at the price specified at the outset of the contract

## Relationships

- **Subclass of**: [Forward](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/Forward.md)

## Constraints

- **[hasDividendAdjustmentPeriod](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/hasDividendAdjustmentPeriod.md)**: some values from of type [DividendAdjustmentPeriod](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/DividendAdjustmentPeriod.md)
- **[hasMethodOfAdjustment](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/hasMethodOfAdjustment.md)**: some values from of type [ForwardContractAdjustmentMethod](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/ForwardContractAdjustmentMethod.md)
- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N234b453206934b90a71c465bc6be0444`
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)

## Annotations

- **label** (en): equity forward
- **definition** (en): forward contract to buy or sell the underlying equity stock, equity index, basket of equity stock, equity futures contract, or equity option at a specified future date at the price specified at the outset of the contract
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
