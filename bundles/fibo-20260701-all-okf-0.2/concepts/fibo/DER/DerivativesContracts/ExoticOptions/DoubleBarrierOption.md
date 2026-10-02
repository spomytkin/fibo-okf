---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: double barrier option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: barrier option applied to currencies or over the counter stocks that works as a binary, or digital option in that
      it pays out only under defined circumstances, or it is worthless, at expiration
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Considered an exotic option, a double barrier option is a combination of two single barrier options, with one barrier
      above and one barrier below the current price of the underlying. It is a bet by the holder that the underlying asset
      will move significantly, in the case of a knock-in barrier option, or will move by a very small amount, in the case
      of a knock-out barrier option, over the life of the contract. Traders use these options when they have an opinion on
      volatility but not on the direction of the underlying asset's next price move. A barrier option is a type of option
      where the payoff, and the very existence of the option, depends on whether or not the underlying asset reaches a predetermined
      price.
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
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasSecondBarrierPrice
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasSecondRebateAmount
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DoubleBarrierOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: double barrier option
type: Ontology Class
---

# double barrier option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DoubleBarrierOption>

## Definition

barrier option applied to currencies or over the counter stocks that works as a binary, or digital option in that it pays out only under defined circumstances, or it is worthless, at expiration

## Relationships

- **Subclass of**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)

## Constraints

- **[hasFirstBarrierPrice](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasFirstBarrierPrice.md)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasFirstRebateAmount](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasFirstRebateAmount.md)**: min qualified cardinality 0 of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- **[hasSecondBarrierPrice](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasSecondBarrierPrice.md)**: some values from of type [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **[hasSecondRebateAmount](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasSecondRebateAmount.md)**: min qualified cardinality 0 of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label** (en): double barrier option
- **definition** (en): barrier option applied to currencies or over the counter stocks that works as a binary, or digital option in that it pays out only under defined circumstances, or it is worthless, at expiration
- **explanatoryNote** (en): Considered an exotic option, a double barrier option is a combination of two single barrier options, with one barrier above and one barrier below the current price of the underlying. It is a bet by the holder that the underlying asset will move significantly, in the case of a knock-in barrier option, or will move by a very small amount, in the case of a knock-out barrier option, over the life of the contract. Traders use these options when they have an opinion on volatility but not on the direction of the underlying asset's next price move. A barrier option is a type of option where the payoff, and the very existence of the option, depends on whether or not the underlying asset reaches a predetermined price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
