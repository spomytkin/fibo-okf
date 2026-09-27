---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: clean price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument price that does not include accrued interest
  disjoint_with:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CleanPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: clean price
type: Ontology Class
---

# clean price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CleanPrice>

## Definition

debt instrument price that does not include accrued interest

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Constraints

- **Disjoint with**: [DirtyPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice.md)

## Annotations

- **label** (en): clean price
- **definition** (en): debt instrument price that does not include accrued interest

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
