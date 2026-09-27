---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has trading date time
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the specific date and time associated with a given price
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasTradingDateTime
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has trading date time
type: Ontology Property
---

# has trading date time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasTradingDateTime>

## Definition

indicates the specific date and time associated with a given price

## Relationships

- **Domain**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **Subproperty of**: [hasDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime>)

## Annotations

- **label** (en): has trading date time
- **definition** (en): indicates the specific date and time associated with a given price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
