---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed coupon bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond whose coupon rate and principal amount are fixed at the time of origination or sale and remain constant while
      the security is outstanding
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasInterestPaymentTerms
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: fixed coupon bond
type: Ontology Class
---

# fixed coupon bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponBond>

## Definition

bond whose coupon rate and principal amount are fixed at the time of origination or sale and remain constant while the security is outstanding

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [FixedIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)

## Constraints

- **Disjoint with**: [VariableCouponBond](/concepts/fibo/SEC/Debt/Bonds/VariableCouponBond.md)
- **[hasInterestPaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasInterestPaymentTerms.md)**: some values from of type [FixedCouponTerms](/concepts/fibo/SEC/Debt/Bonds/FixedCouponTerms.md)

## Annotations

- **label**: fixed coupon bond
- **definition**: bond whose coupon rate and principal amount are fixed at the time of origination or sale and remain constant while the security is outstanding

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
