---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: zero coupon bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond issued with a coupon rate of zero and that trades at a deep discount to face value
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fannie Mae also issues zero-coupon callable debt securities. Zero-coupon notes are debt securities on which no
      coupon interest is paid to the investor. Rather, the security is purchased at a discounted dollar price and matures
      at par. If the option on a callable zero-coupon security is exercised, it is redeemed at a higher dollar price than
      the original issue price. The yield for a callable zero-coupon security is based on the difference between the original
      discounted price and the principal payment at the call date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The principal amount accretes over time at a constant accrual rate and is redeemed at full face value at maturity.
      In effect, the accrual rate is the coupon rate or yield which is added to the outstanding principal rather than being
      paid out to investors.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: z-bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasOriginalIssueDiscountAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasInterestPaymentTerms
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: zero coupon bond
type: Ontology Class
---

# zero coupon bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponBond>

## Definition

bond issued with a coupon rate of zero and that trades at a deep discount to face value

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [FixedIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)

## Constraints

- **[hasOriginalIssueDiscountAmount](/concepts/fibo/SEC/Debt/Bonds/hasOriginalIssueDiscountAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasInterestPaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasInterestPaymentTerms.md)**: some values from of type [ZeroCouponTerms](/concepts/fibo/SEC/Debt/Bonds/ZeroCouponTerms.md)
- **[hasRelativePriceAtMaturity](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue`

## Annotations

- **label**: zero coupon bond
- **definition**: bond issued with a coupon rate of zero and that trades at a deep discount to face value
- **explanatoryNote**: Fannie Mae also issues zero-coupon callable debt securities. Zero-coupon notes are debt securities on which no coupon interest is paid to the investor. Rather, the security is purchased at a discounted dollar price and matures at par. If the option on a callable zero-coupon security is exercised, it is redeemed at a higher dollar price than the original issue price. The yield for a callable zero-coupon security is based on the difference between the original discounted price and the principal payment at the call date.
- **explanatoryNote**: The principal amount accretes over time at a constant accrual rate and is redeemed at full face value at maturity. In effect, the accrual rate is the coupon rate or yield which is added to the outstanding principal rather than being paid out to investors.
- **synonym**: z-bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
