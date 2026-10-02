---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bid price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price a prospective buyer is willing to pay
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The term 'bid price' is used by traders / market makers with respect to a given security, and that are prepared
      to buy or sell round lots at publicly quoted prices, and by specialists in certain instruments that perform similar
      functions on an exchange.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OfferPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BidPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: bid price
type: Ontology Class
---

# bid price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BidPrice>

## Definition

price a prospective buyer is willing to pay

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Constraints

- **Disjoint with**: [OfferPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md)

## Annotations

- **label** (en): bid price
- **definition** (en): price a prospective buyer is willing to pay
- **explanatoryNote** (en): The term 'bid price' is used by traders / market makers with respect to a given security, and that are prepared to buy or sell round lots at publicly quoted prices, and by specialists in certain instruments that perform similar functions on an exchange.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
