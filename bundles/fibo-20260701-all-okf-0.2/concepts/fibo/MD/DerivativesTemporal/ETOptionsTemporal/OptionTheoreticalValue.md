---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option theoretical value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: fair value of the option as determined by an option pricing model
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The pricing model (such as the Black-Scholes model) takes into account current values such as implied volatility,
      the price of the underlying, the strike price, and time to expiration to determine what an option should be worth. Each
      of the input values fluctuate, which means theoretical price will also be a fluctuating value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PricingModel
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionTheoreticalValue
sources:
- id: fibo-source-c9fb3c7ad1
  resource: references/fibo/MD/DerivativesTemporal/ETOptionsTemporal.rdf
  sha256: c9fb3c7ad151168ecfeee8fa19d4cecdedf784d117c95c63d88ddd4c69e32f13
  title: FIBO source MD/DerivativesTemporal/ETOptionsTemporal.rdf
title: option theoretical value
type: Ontology Class
---

# option theoretical value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionTheoreticalValue>

## Definition

fair value of the option as determined by an option pricing model

## Relationships

- **Subclass of**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [PricingModel](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PricingModel.md)

## Annotations

- **label** (en): option theoretical value
- **definition** (en): fair value of the option as determined by an option pricing model
- **explanatoryNote** (en): The pricing model (such as the Black-Scholes model) takes into account current values such as implied volatility, the price of the underlying, the strike price, and time to expiration to determine what an option should be worth. Each of the input values fluctuate, which means theoretical price will also be a fluctuating value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
