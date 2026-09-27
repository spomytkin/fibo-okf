---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: best bid
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: highest bid price a prospective buyer is willing to pay at a particular time for a given security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BidPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BestBid
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: best bid
type: Ontology Class
---

# best bid

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BestBid>

## Definition

highest bid price a prospective buyer is willing to pay at a particular time for a given security

## Relationships

- **Subclass of**: [BidPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md)

## Constraints

- **[hasApplicablePeriod](<https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod>)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): best bid
- **definition** (en): highest bid price a prospective buyer is willing to pay at a particular time for a given security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
