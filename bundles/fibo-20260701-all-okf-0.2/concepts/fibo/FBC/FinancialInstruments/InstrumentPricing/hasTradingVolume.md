---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has trading volume
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of shares/units traded on a given trading day
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasTradingVolume
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has trading volume
type: Ontology Property
---

# has trading volume

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasTradingVolume>

## Definition

indicates the number of shares/units traded on a given trading day

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)

## Annotations

- **label** (en): has trading volume
- **definition** (en): indicates the number of shares/units traded on a given trading day

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
