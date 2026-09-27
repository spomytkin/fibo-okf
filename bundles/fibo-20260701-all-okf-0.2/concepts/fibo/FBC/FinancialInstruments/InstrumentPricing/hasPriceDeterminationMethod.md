---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has price determination method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a strategy by which a given price is determined
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: has price determination method
type: Ontology Property
---

# has price determination method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPriceDeterminationMethod>

## Definition

indicates a strategy by which a given price is determined

## Relationships

- **Range**: [PriceDeterminationMethod](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
- **Subproperty of**: [hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)

## Annotations

- **label** (en): has price determination method
- **definition** (en): indicates a strategy by which a given price is determined

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
