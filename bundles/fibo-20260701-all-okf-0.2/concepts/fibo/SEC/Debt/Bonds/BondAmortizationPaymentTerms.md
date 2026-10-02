---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond amortization payment terms
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms that include a schedule for repayment of the principal over the lifetime of the bond, typically in equal
      payments at regular intervals
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/AmortizationSchedule
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasSchedule
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondPrincipalRepaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond amortization payment terms
type: Ontology Class
---

# bond amortization payment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms>

## Definition

terms that include a schedule for repayment of the principal over the lifetime of the bond, typically in equal payments at regular intervals

## Relationships

- **Subclass of**: [BondPrincipalRepaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md)

## Constraints

- **Disjoint with**: [BulletPrincipalRepaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BulletPrincipalRepaymentTerms.md)
- **[hasSchedule](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasSchedule.md)**: some values from of type [AmortizationSchedule](/concepts/fibo/FBC/DebtAndEquities/Debt/AmortizationSchedule.md)

## Annotations

- **label**: bond amortization payment terms
- **definition**: terms that include a schedule for repayment of the principal over the lifetime of the bond, typically in equal payments at regular intervals

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
