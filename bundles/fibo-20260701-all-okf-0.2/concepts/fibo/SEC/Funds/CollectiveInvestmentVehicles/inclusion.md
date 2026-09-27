---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inclusion
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether the referred strategy is included. No means this description refers to the exclusion of what is described,
      from the portfolio.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/inclusion
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: inclusion
type: Ontology Property
---

# inclusion

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/inclusion>

## Definition

Whether the referred strategy is included. No means this description refers to the exclusion of what is described, from the portfolio.

## Relationships

- **Domain**: [FundPortfolioInvestmentLimitations](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): inclusion
- **definition** (en): Whether the referred strategy is included. No means this description refers to the exclusion of what is described, from the portfolio.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
