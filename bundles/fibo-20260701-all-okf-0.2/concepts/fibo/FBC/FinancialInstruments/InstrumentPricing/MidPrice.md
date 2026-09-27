---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mid price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: arithmetic mean between bid and offer prices
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BidPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OfferPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
  - concept: /concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/MidPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: mid price
type: Ontology Class
---

# mid price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/MidPrice>

## Definition

arithmetic mean between bid and offer prices

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **Subclass of**: [ArithmeticMean](/concepts/fibo/FND/Utilities/Analytics/ArithmeticMean.md)

## Constraints

- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasApplicablePeriod](<https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod>)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [BidPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [OfferPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md)

## Annotations

- **label** (en): mid price
- **definition** (en): arithmetic mean between bid and offer prices

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
