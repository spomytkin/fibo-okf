---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund bond unit coupon
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A fixed coupon paid out to holders of the Fund Bond Unit.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/hasPolicyTerms
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund bond unit coupon
type: Ontology Class
---

# fund bond unit coupon

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundBondUnitCoupon>

## Definition

A fixed coupon paid out to holders of the Fund Bond Unit.

## Relationships

- **Subclass of**: [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)

## Constraints

- **[hasPolicyTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/hasPolicyTerms.md)**: some values from of type [FundCouponPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy.md)

## Annotations

- **label** (en): fund bond unit coupon
- **definition** (en): A fixed coupon paid out to holders of the Fund Bond Unit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
