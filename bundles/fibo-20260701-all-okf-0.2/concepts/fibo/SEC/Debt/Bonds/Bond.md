---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tradable debt instrument representing a loan in which the issuer owes the holder(s) a debt
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Depending on the terms of the contract, the issuer is obliged to pay interest (the coupon) and/or to repay the
      principal at maturity. The most common bonds are corporate or governmental, typically used to finance specific projects
      or operations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasInterestPaymentTerms
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondPrincipalRepaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRepaymentTerms
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasSeries
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidAtMaturity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidAtMaturity
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond
type: Ontology Class
---

# bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond>

## Definition

tradable debt instrument representing a loan in which the issuer owes the holder(s) a debt

## Relationships

- **Subclass of**: [CreditAgreementRepaidAtMaturity](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidAtMaturity.md)
- **Subclass of**: [TradableDebtInstrument](/concepts/fibo/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)

## Constraints

- **[hasInterestPaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasInterestPaymentTerms.md)**: some values from of type [CouponPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md)
- **[hasRepaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasRepaymentTerms.md)**: some values from of type [BondPrincipalRepaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md)
- **[hasSeries](/concepts/fibo/SEC/Securities/SecuritiesIssuance/hasSeries.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: bond
- **definition**: tradable debt instrument representing a loan in which the issuer owes the holder(s) a debt
- **explanatoryNote**: Depending on the terms of the contract, the issuer is obliged to pay interest (the coupon) and/or to repay the principal at maturity. The most common bonds are corporate or governmental, typically used to finance specific projects or operations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
