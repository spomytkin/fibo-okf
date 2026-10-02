---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: holder may reinvest
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether or not the holder may reinvest dividends in the fund.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/DistributingShareClass.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/DistributingShareClass
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/holderMayReinvest
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: holder may reinvest
type: Ontology Property
---

# holder may reinvest

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/holderMayReinvest>

## Definition

Whether or not the holder may reinvest dividends in the fund.

## Relationships

- **Domain**: [DistributingShareClass](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/DistributingShareClass.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): holder may reinvest
- **definition** (en): Whether or not the holder may reinvest dividends in the fund.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
