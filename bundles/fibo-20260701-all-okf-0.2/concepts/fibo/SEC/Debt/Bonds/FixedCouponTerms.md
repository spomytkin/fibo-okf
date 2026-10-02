---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed coupon terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms for payment of interest on a bond with a fixed interest rate
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableCouponTerms.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/FixedInterestRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: fixed coupon terms
type: Ontology Class
---

# fixed coupon terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponTerms>

## Definition

terms for payment of interest on a bond with a fixed interest rate

## Relationships

- **Subclass of**: [CouponPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md)

## Constraints

- **Disjoint with**: [VariableCouponTerms](/concepts/fibo/SEC/Debt/Bonds/VariableCouponTerms.md)
- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [FixedInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/FixedInterestRate.md)

## Annotations

- **label**: fixed coupon terms
- **definition**: terms for payment of interest on a bond with a fixed interest rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
