---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has closing price determination method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a strategy by which the official closing price is determined
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This method itself changes quite frequently i.e. the exchange may change the way it computes closing prices.
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasClosingPriceDeterminationMethod
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has closing price determination method
type: Ontology Property
---

# has closing price determination method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasClosingPriceDeterminationMethod>

## Definition

indicates a strategy by which the official closing price is determined

## Relationships

- **Range**: [ClosingPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod.md)
- **Subproperty of**: [hasPriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod.md)

## Annotations

- **label** (en): has closing price determination method
- **definition** (en): indicates a strategy by which the official closing price is determined
- **explanatoryNote** (en): This method itself changes quite frequently i.e. the exchange may change the way it computes closing prices.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
