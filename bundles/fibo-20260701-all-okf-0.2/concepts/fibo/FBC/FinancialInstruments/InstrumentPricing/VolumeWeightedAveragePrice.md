---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: volume-weighted average price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: average price at which a given security has traded throughout a trading day, determined by multiplying each trade
      by its volume, adding the results, then dividing by the volume traded for the day
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: VWAP
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/VolumeWeightedAveragePrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: volume-weighted average price
type: Ontology Class
---

# volume-weighted average price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/VolumeWeightedAveragePrice>

## Definition

average price at which a given security has traded throughout a trading day, determined by multiplying each trade by its volume, adding the results, then dividing by the volume traded for the day

## Relationships

- **Subclass of**: [PriceAnalytic](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md)

## Annotations

- **label** (en): volume-weighted average price
- **definition** (en): average price at which a given security has traded throughout a trading day, determined by multiplying each trade by its volume, adding the results, then dividing by the volume traded for the day
- **abbreviation** (en): VWAP

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
