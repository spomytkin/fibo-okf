---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: coupon payment terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms for payment of interest on a bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondCoupon
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: coupon payment terms
type: Ontology Class
---

# coupon payment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms>

## Definition

terms for payment of interest on a bond

## Relationships

- **Subclass of**: [InterestPaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [BondCoupon](/concepts/fibo/SEC/Debt/Bonds/BondCoupon.md)
- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: some values from of type [InterestPaymentSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentSchedule.md)

## Annotations

- **label**: coupon payment terms
- **definition**: terms for payment of interest on a bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
