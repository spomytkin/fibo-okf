---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity portfolio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A portfolio which has at least 85% exposure to shares.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholding
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/EquityPortfolio
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: equity portfolio
type: Ontology Class
---

# equity portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/EquityPortfolio>

## Definition

A portfolio which has at least 85% exposure to shares.

## Relationships

- **Subclass of**: [FundPortfolio](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [Shareholding](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholding.md)

## Annotations

- **label** (en): equity portfolio
- **definition** (en): A portfolio which has at least 85% exposure to shares.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
