---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ex coupon date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The date at which the coupon is substracted from the NAV
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy
  range:
  - concept: /concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/DayOfMonth
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/exCouponDate
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: ex coupon date
type: Ontology Property
---

# ex coupon date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/exCouponDate>

## Definition

The date at which the coupon is substracted from the NAV

## Relationships

- **Domain**: [FundCouponPolicy](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundCouponPolicy.md)
- **Range**: [DayOfMonth](/concepts/fibo/FND/DatesAndTimes/BusinessDates/DayOfMonth.md)

## Annotations

- **label** (en): ex coupon date
- **definition** (en): The date at which the coupon is substracted from the NAV

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
