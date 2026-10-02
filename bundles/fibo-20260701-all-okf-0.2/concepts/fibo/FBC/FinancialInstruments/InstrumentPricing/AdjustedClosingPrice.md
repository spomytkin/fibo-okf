---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: adjusted closing price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: amended closing price to reflect a security's value after accounting for any corporate actions, such as stock splits,
      dividends, and rights offerings
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A particularly dramatic change in price occurs when a company announces a stock split. When the change is made,
      the price displayed will immediately reflect the split. For example, if a company splits its stock 2-for-1, the last
      closing price will be cut in half. That's the adjusted closing price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/AdjustedClosingPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: adjusted closing price
type: Ontology Class
---

# adjusted closing price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/AdjustedClosingPrice>

## Definition

amended closing price to reflect a security's value after accounting for any corporate actions, such as stock splits, dividends, and rights offerings

## Relationships

- **Subclass of**: [ClosingPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md)

## Annotations

- **label** (en): adjusted closing price
- **definition** (en): amended closing price to reflect a security's value after accounting for any corporate actions, such as stock splits, dividends, and rights offerings
- **explanatoryNote** (en): A particularly dramatic change in price occurs when a company announces a stock split. When the change is made, the price displayed will immediately reflect the split. For example, if a company splits its stock 2-for-1, the last closing price will be cut in half. That's the adjusted closing price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
