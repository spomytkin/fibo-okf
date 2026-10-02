---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: options greek
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: quantity representing the sensitivity of the price of an option or options to a change in underlying parameters
      on which the value depends
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek
sources:
- id: fibo-source-c9fb3c7ad1
  resource: references/fibo/MD/DerivativesTemporal/ETOptionsTemporal.rdf
  sha256: c9fb3c7ad151168ecfeee8fa19d4cecdedf784d117c95c63d88ddd4c69e32f13
  title: FIBO source MD/DerivativesTemporal/ETOptionsTemporal.rdf
title: options greek
type: Ontology Class
---

# options greek

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionsGreek>

## Definition

quantity representing the sensitivity of the price of an option or options to a change in underlying parameters on which the value depends

## Relationships

- **Subclass of**: [PriceAnalytic](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md)

## Annotations

- **label** (en): options greek
- **definition** (en): quantity representing the sensitivity of the price of an option or options to a change in underlying parameters on which the value depends

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
