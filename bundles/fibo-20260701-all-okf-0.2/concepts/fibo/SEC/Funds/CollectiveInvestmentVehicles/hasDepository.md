---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has depository
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
  range:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDepository
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: has depository
type: Ontology Property
---

# has depository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasDepository>

## Relationships

- **Domain**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
- **Range**: [FundDepositary](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary.md)
- **Subproperty of**: [fundHasRelatedParty](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/fundHasRelatedParty.md)

## Annotations

- **label** (en): has depository

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
