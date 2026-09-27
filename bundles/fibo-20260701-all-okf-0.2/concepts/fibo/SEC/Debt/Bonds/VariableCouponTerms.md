---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable coupon terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractual terms specifying the calculation of the interest rate for a variable coupon bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableInterestCalculationFormula
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: variable coupon terms
type: Ontology Class
---

# variable coupon terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableCouponTerms>

## Definition

contractual terms specifying the calculation of the interest rate for a variable coupon bond

## Relationships

- **Subclass of**: [CouponPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: some values from of type [VariableInterestCalculationFormula](/concepts/fibo/SEC/Debt/Bonds/VariableInterestCalculationFormula.md)

## Annotations

- **label**: variable coupon terms
- **definition**: contractual terms specifying the calculation of the interest rate for a variable coupon bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
