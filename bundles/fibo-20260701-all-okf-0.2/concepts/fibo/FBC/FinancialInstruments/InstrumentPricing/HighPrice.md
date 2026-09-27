---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: high price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: highest price for a given security over the period specified
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/HighPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: high price
type: Ontology Class
---

# high price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/HighPrice>

## Definition

highest price for a given security over the period specified

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Constraints

- **[hasApplicablePeriod](<https://www.omg.org/spec/Commons/ContextualDesignators/hasApplicablePeriod>)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label** (en): high price
- **definition** (en): highest price for a given security over the period specified

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
