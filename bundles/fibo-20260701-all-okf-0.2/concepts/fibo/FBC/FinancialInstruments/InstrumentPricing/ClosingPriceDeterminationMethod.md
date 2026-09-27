---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: closing price determination method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: strategy for calculating or otherwise determining an official closing price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The official closing price is typically the final price at which something trades during regular market hours on
      an exchange or trading venue. Because of the evolving nature of online trading in a 24 hour world, every exchange has
      a method of calculating its official closing price, although that methodology changes from time to time. They may also
      publish an adjusted closing price, which reflects changes to the price that reflect corporate actions and after hours
      trading that occur before the opening of the exchange on the following day. Understanding how the closing price is determined
      is important to ensure price comparability for a given security across exchanges.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: closing price determination method
type: Ontology Class
---

# closing price determination method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod>

## Definition

strategy for calculating or otherwise determining an official closing price

## Relationships

- **Subclass of**: [PriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)

## Annotations

- **label** (en): closing price determination method
- **definition** (en): strategy for calculating or otherwise determining an official closing price
- **explanatoryNote** (en): The official closing price is typically the final price at which something trades during regular market hours on an exchange or trading venue. Because of the evolving nature of online trading in a 24 hour world, every exchange has a method of calculating its official closing price, although that methodology changes from time to time. They may also publish an adjusted closing price, which reflects changes to the price that reflect corporate actions and after hours trading that occur before the opening of the exchange on the following day. Understanding how the closing price is determined is important to ensure price comparability for a given security across exchanges.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
