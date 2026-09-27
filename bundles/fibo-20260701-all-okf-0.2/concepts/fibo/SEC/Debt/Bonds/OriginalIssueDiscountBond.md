---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: original issue discount bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest-bearing bond issued at a deep discount to face value
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An original issue discount (OID) is the discount in price from a bond's face value at the time a bond or other
      debt instrument is first issued. The OID is the amount of discount or the difference between the original face value
      and the price paid for the bond.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The principal amount accretes over time at a constant accrual rate and is redeemed at full face value at maturity.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: OID bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasOriginalIssueDiscountAmount
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/OriginalIssueDiscountBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: original issue discount bond
type: Ontology Class
---

# original issue discount bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/OriginalIssueDiscountBond>

## Definition

interest-bearing bond issued at a deep discount to face value

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Constraints

- **[hasOriginalIssueDiscountAmount](/concepts/fibo/SEC/Debt/Bonds/hasOriginalIssueDiscountAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasRelativePriceAtMaturity](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue`

## Annotations

- **label**: original issue discount bond
- **definition**: interest-bearing bond issued at a deep discount to face value
- **explanatoryNote**: An original issue discount (OID) is the discount in price from a bond's face value at the time a bond or other debt instrument is first issued. The OID is the amount of discount or the difference between the original face value and the price paid for the bond.
- **explanatoryNote**: The principal amount accretes over time at a constant accrual rate and is redeemed at full face value at maturity.
- **synonym**: OID bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
