---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: knock-in option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: barrier option that is not triggered until a certain price threshold is met
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Assume an investor purchases a knock-in put option with a down Direction, with a barrier price of $90 and a strike
      price of $100. The underlying security is trading at $110, and the option expires in three months. If the price of the
      underlying security reaches $90, the option comes into existence and becomes a vanilla option with a strike price of
      $100. Thereafter, the holder of the option has the right to sell the underlying asset at the strike price of $100, even
      though it is trading below $90. It is this right that gives the option value. The put option remains active until the
      expiration date, even if the underlying security rebounds back above $90. However, if the underlying asset does not
      fall below the barrier price during the life of the contract, the down-and-in option expires worthless. Just because
      the barrier is reached does not assure a profit on the trade since the underlying would need to stay below $100 (after
      triggering the barrier) in order for the option to have value.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the price is never reached, it is as if the contract never existed. However, if the underlying asset reaches
      a specified barrier, the knock-in option comes into existence. The difference between a knock-in and knock-out option
      is that a knock-in option comes into existence only when the underlying security reaches a barrier, while a knock-out
      option ceases to exist when the underlying security reaches a barrier.
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
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockInOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: knock-in option
type: Ontology Class
---

# knock-in option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockInOption>

## Definition

barrier option that is not triggered until a certain price threshold is met

## Relationships

- **Subclass of**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)

## Constraints

- **[hasFirstBarrierPrice](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasFirstBarrierPrice.md)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasFirstRebateAmount](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasFirstRebateAmount.md)**: min qualified cardinality 0 of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label** (en): knock-in option
- **definition** (en): barrier option that is not triggered until a certain price threshold is met
- **example** (en): Assume an investor purchases a knock-in put option with a down Direction, with a barrier price of $90 and a strike price of $100. The underlying security is trading at $110, and the option expires in three months. If the price of the underlying security reaches $90, the option comes into existence and becomes a vanilla option with a strike price of $100. Thereafter, the holder of the option has the right to sell the underlying asset at the strike price of $100, even though it is trading below $90. It is this right that gives the option value. The put option remains active until the expiration date, even if the underlying security rebounds back above $90. However, if the underlying asset does not fall below the barrier price during the life of the contract, the down-and-in option expires worthless. Just because the barrier is reached does not assure a profit on the trade since the underlying would need to stay below $100 (after triggering the barrier) in order for the option to have value.
- **explanatoryNote** (en): If the price is never reached, it is as if the contract never existed. However, if the underlying asset reaches a specified barrier, the knock-in option comes into existence. The difference between a knock-in and knock-out option is that a knock-in option comes into existence only when the underlying security reaches a barrier, while a knock-out option ceases to exist when the underlying security reaches a barrier.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
