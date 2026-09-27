---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: opening price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price at which something first trades at the start of a trading day
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Investors that want to buy or sell as soon as the market opens will put in an order at the opening price. Depending
      on how the closing price for the prior day is determined, and if there is no after hours trading (AFT), the opening
      price will be the same as the prior trading day's closing price. Otherwise, the opening price may differ from the prior
      trading day's official closing price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/MarketPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OpeningPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: opening price
type: Ontology Class
---

# opening price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OpeningPrice>

## Definition

price at which something first trades at the start of a trading day

## Relationships

- **Subclass of**: [MarketPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md)

## Annotations

- **label** (en): opening price
- **definition** (en): price at which something first trades at the start of a trading day
- **explanatoryNote** (en): Investors that want to buy or sell as soon as the market opens will put in an order at the opening price. Depending on how the closing price for the prior day is determined, and if there is no after hours trading (AFT), the opening price will be the same as the prior trading day's closing price. Otherwise, the opening price may differ from the prior trading day's official closing price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
