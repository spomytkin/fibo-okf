---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: zero coupon terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms for payment of interest on a zero coupon bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroInterestRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms
  - concept: /concepts/fibo/SEC/Debt/Bonds/FixedCouponTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: zero coupon terms
type: Ontology Class
---

# zero coupon terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponTerms>

## Definition

terms for payment of interest on a zero coupon bond

## Relationships

- **Subclass of**: [BondAmortizationPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
- **Subclass of**: [FixedCouponTerms](/concepts/fibo/SEC/Debt/Bonds/FixedCouponTerms.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroInterestRate`

## Annotations

- **label**: zero coupon terms
- **definition**: terms for payment of interest on a zero coupon bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
