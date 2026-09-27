---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: official closing price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price of the final trade of a security at the end of a trading day on a given exchange
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A stock's closing price is the standard benchmark used by investors to track its performance over time.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: end-of-day price
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasClosingPriceDeterminationMethod
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OfficialClosingPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: official closing price
type: Ontology Class
---

# official closing price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OfficialClosingPrice>

## Definition

price of the final trade of a security at the end of a trading day on a given exchange

## Relationships

- **Subclass of**: [ClosingPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md)

## Constraints

- **[hasClosingPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasClosingPriceDeterminationMethod.md)**: some values from of type [ClosingPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod.md)

## Annotations

- **label** (en): official closing price
- **definition** (en): price of the final trade of a security at the end of a trading day on a given exchange
- **explanatoryNote** (en): A stock's closing price is the standard benchmark used by investors to track its performance over time.
- **synonym** (en): end-of-day price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
