---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited shares are issued
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether or not new shares can be issued in the fund. This is what makes it a closed end or open end fund.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/limitedSharesAreIssued
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: limited shares are issued
type: Ontology Property
---

# limited shares are issued

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/limitedSharesAreIssued>

## Definition

Whether or not new shares can be issued in the fund. This is what makes it a closed end or open end fund.

## Relationships

- **Domain**: [FundShareClassUnit](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): limited shares are issued
- **definition** (en): Whether or not new shares can be issued in the fund. This is what makes it a closed end or open end fund.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
