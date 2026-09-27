---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: best offer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lowest price acceptable to a prospective seller for a given security at a particular point in time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OfferPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BestOffer
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: best offer
type: Ontology Class
---

# best offer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BestOffer>

## Definition

lowest price acceptable to a prospective seller for a given security at a particular point in time

## Relationships

- **Subclass of**: [OfferPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md)

## Constraints

- **[hasApplicablePeriod](<https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod>)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): best offer
- **definition** (en): lowest price acceptable to a prospective seller for a given security at a particular point in time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
