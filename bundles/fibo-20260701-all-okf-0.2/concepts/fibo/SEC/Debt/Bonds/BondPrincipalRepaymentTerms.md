---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond principal repayment terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms for the repayment of the principal on a bond
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondPrincipalRepaymentTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond principal repayment terms
type: Ontology Class
---

# bond principal repayment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondPrincipalRepaymentTerms>

## Definition

terms for the repayment of the principal on a bond

## Relationships

- **Subclass of**: [PrincipalRepaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)

## Constraints

- **Disjoint with**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: some values from of type [PaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentSchedule.md)

## Annotations

- **label**: bond principal repayment terms
- **definition**: terms for the repayment of the principal on a bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
