---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable coupon bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that has a floating interest rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The rate adjusts according to a predetermined formula outlined in the bond's prospectus or official statement.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondVariableCoupon
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariableIncomeBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableIncomeBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: variable coupon bond
type: Ontology Class
---

# variable coupon bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponBond>

## Definition

bond that has a floating interest rate

## Relationships

- **Subclass of**: [VariableIncomeBond](/concepts/fibo/SEC/Debt/Bonds/VariableIncomeBond.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [BondVariableCoupon](/concepts/fibo/SEC/Debt/Bonds/BondVariableCoupon.md)

## Annotations

- **label**: variable coupon bond
- **definition**: bond that has a floating interest rate
- **explanatoryNote**: The rate adjusts according to a predetermined formula outlined in the bond's prospectus or official statement.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
