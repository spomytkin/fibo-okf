---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: portfolio benchmark
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Security or other price against which the performance of the portfolio is evaluated.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/definesBenchmark
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Measure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: portfolio benchmark
type: Ontology Class
---

# portfolio benchmark

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark>

## Definition

Security or other price against which the performance of the portfolio is evaluated.

## Relationships

- **Subclass of**: [Measure](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Measure>)

## Constraints

- **[definesBenchmark](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/definesBenchmark.md)**: some values from of type [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [FundPortfolio](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md)

## Annotations

- **label** (en): portfolio benchmark
- **definition** (en): Security or other price against which the performance of the portfolio is evaluated.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
