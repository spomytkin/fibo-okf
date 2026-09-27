---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: futures greek
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: quantity representing the sensitivity of the price of a future or futures to a change in underlying parameters
      on which the value depends
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/FuturesGreek
sources:
- id: fibo-source-c2e233cb71
  resource: references/fibo/MD/DerivativesTemporal/FuturesTemporal.rdf
  sha256: c2e233cb71a6057762c1da19bf2b1316166cd651fcf570e55af51b91c70f41c5
  title: FIBO source MD/DerivativesTemporal/FuturesTemporal.rdf
title: futures greek
type: Ontology Class
---

# futures greek

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/FuturesGreek>

## Definition

quantity representing the sensitivity of the price of a future or futures to a change in underlying parameters on which the value depends

## Relationships

- **Subclass of**: [PriceAnalytic](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md)

## Annotations

- **label** (en): futures greek
- **definition** (en): quantity representing the sensitivity of the price of a future or futures to a change in underlying parameters on which the value depends

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
