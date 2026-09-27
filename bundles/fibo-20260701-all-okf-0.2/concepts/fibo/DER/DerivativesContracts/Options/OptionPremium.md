---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option premium
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: current market price of an option contract
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The option premium is the income received by the seller (writer) of an option contract to another party. In-the-money
      option premiums are composed of two factors: intrinsic and extrinsic value. Out-of-the-money options'' premiums consist
      solely of extrinsic value. For stock options, the premium is quoted as a dollar amount per share, and most contracts
      represent the commitment of 100 shares.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremiumFormula
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/MarketPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremium
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: option premium
type: Ontology Class
---

# option premium

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremium>

## Definition

current market price of an option contract

## Relationships

- **Subclass of**: [MarketPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md)

## Constraints

- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: min qualified cardinality 0 of type [OptionPremiumFormula](/concepts/fibo/DER/DerivativesContracts/Options/OptionPremiumFormula.md)
- **[hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)**: min qualified cardinality 0 of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label** (en): option premium
- **definition** (en): current market price of an option contract
- **explanatoryNote** (en): The option premium is the income received by the seller (writer) of an option contract to another party. In-the-money option premiums are composed of two factors: intrinsic and extrinsic value. Out-of-the-money options' premiums consist solely of extrinsic value. For stock options, the premium is quoted as a dollar amount per share, and most contracts represent the commitment of 100 shares.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
