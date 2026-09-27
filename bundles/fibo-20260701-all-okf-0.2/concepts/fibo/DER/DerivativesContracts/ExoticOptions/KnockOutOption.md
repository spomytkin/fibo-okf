---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: knock-out option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: barrier option with a built-in mechanism to expire as worthless if a specified price level in the underlying asset
      is reached
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Assume an investor purchases a Knock-Out call option with a down Direction, also called a 'Down and Out Option',
      on a stock that is trading at $60 with a strike price of $55 and a barrier of $50. Assume the stock trades below $50,
      at any time, before the call option expires. Therefore, the down-and-out call option promptly ceases to exist.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A knock-out option sets a cap on the level an option can reach in the holder's favor. As knock-out options limit
      the profit potential for the option buyer, they can be purchased for a smaller premium than an equivalent option without
      a knock-out stipulation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasFirstBarrierPrice
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasFirstRebateAmount
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockOutOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: knock-out option
type: Ontology Class
---

# knock-out option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockOutOption>

## Definition

barrier option with a built-in mechanism to expire as worthless if a specified price level in the underlying asset is reached

## Relationships

- **Subclass of**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)

## Constraints

- **[hasFirstBarrierPrice](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasFirstBarrierPrice.md)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasFirstRebateAmount](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasFirstRebateAmount.md)**: min qualified cardinality 0 of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label** (en): knock-out option
- **definition** (en): barrier option with a built-in mechanism to expire as worthless if a specified price level in the underlying asset is reached
- **example** (en): Assume an investor purchases a Knock-Out call option with a down Direction, also called a 'Down and Out Option', on a stock that is trading at $60 with a strike price of $55 and a barrier of $50. Assume the stock trades below $50, at any time, before the call option expires. Therefore, the down-and-out call option promptly ceases to exist.
- **explanatoryNote** (en): A knock-out option sets a cap on the level an option can reach in the holder's favor. As knock-out options limit the profit potential for the option buyer, they can be purchased for a smaller premium than an equivalent option without a knock-out stipulation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
