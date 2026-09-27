---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond variable coupon
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond coupon that has a variable interest rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/VariableInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/VariableInterestRate
  - concept: /concepts/fibo/SEC/Debt/Bonds/BondCoupon.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondCoupon
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondVariableCoupon
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond variable coupon
type: Ontology Class
---

# bond variable coupon

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondVariableCoupon>

## Definition

bond coupon that has a variable interest rate

## Relationships

- **Subclass of**: [VariableInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/VariableInterestRate.md)
- **Subclass of**: [BondCoupon](/concepts/fibo/SEC/Debt/Bonds/BondCoupon.md)

## Annotations

- **label**: bond variable coupon
- **definition**: bond coupon that has a variable interest rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
