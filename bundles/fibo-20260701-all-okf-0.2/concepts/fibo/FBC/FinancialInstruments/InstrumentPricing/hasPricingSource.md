---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has pricing source
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the origin of a given quote or price for a financial instrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has pricing source
type: Ontology Property
---

# has pricing source

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource>

## Definition

indicates the origin of a given quote or price for a financial instrument

## Relationships

- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label** (en): has pricing source
- **definition** (en): indicates the origin of a given quote or price for a financial instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
