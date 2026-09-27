---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment focus
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The information about the area the fund is mostly invested into (for example stock market in Germany).
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/investmentFocus
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: investment focus
type: Ontology Property
---

# investment focus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/investmentFocus>

## Definition

The information about the area the fund is mostly invested into (for example stock market in Germany).

## Relationships

- **Domain**: [PortfolioInvestmentStrategy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): investment focus
- **definition** (en): The information about the area the fund is mostly invested into (for example stock market in Germany).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
