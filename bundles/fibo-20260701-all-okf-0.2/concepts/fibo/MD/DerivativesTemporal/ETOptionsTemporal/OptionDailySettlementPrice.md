---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option daily settlement price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The official price at the end of a trading session. This price is established by The Options Clearing Corporation
      and is used to determine changes in account equity, margin requirements, and for other purposes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
    value: N46f3353ff5cb4f22bbb1af966374b692
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionDailySettlementPrice
sources:
- id: fibo-source-c9fb3c7ad1
  resource: references/fibo/MD/DerivativesTemporal/ETOptionsTemporal.rdf
  sha256: c9fb3c7ad151168ecfeee8fa19d4cecdedf784d117c95c63d88ddd4c69e32f13
  title: FIBO source MD/DerivativesTemporal/ETOptionsTemporal.rdf
title: option daily settlement price
type: Ontology Class
---

# option daily settlement price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionDailySettlementPrice>

## Definition

The official price at the end of a trading session. This price is established by The Options Clearing Corporation and is used to determine changes in account equity, margin requirements, and for other purposes.

## Relationships

- **Subclass of**: [ClosingPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md)
- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: some values from value `N46f3353ff5cb4f22bbb1af966374b692`

## Annotations

- **label** (en): option daily settlement price
- **definition** (en): The official price at the end of a trading session. This price is established by The Options Clearing Corporation and is used to determine changes in account equity, margin requirements, and for other purposes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
