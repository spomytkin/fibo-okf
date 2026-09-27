---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: minimum investment percentage
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Minimum percentage that has to be invested in the specified strategy.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumInvestmentPercentage
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: minimum investment percentage
type: Ontology Property
---

# minimum investment percentage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/minimumInvestmentPercentage>

## Definition

Minimum percentage that has to be invested in the specified strategy.

## Relationships

- **Domain**: [FundPortfolioInvestmentLimitations](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)
- **Range**: [Percentage](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage>)

## Annotations

- **label** (en): minimum investment percentage
- **definition** (en): Minimum percentage that has to be invested in the specified strategy.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
