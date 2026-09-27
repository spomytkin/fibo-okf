---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: maximum redemption fee
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Maximum percentage or fixed amount of money due when redeeming fund shares Definition origin:EFAMA DD
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Fee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Fee
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/maximumRedemptionFee
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: maximum redemption fee
type: Ontology Property
---

# maximum redemption fee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/maximumRedemptionFee>

## Definition

Maximum percentage or fixed amount of money due when redeeming fund shares Definition origin:EFAMA DD

## Relationships

- **Domain**: [FundSubscriptionTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md)
- **Range**: [Fee](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Fee.md)

## Annotations

- **label** (en): maximum redemption fee
- **definition** (en): Maximum percentage or fixed amount of money due when redeeming fund shares Definition origin:EFAMA DD

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
