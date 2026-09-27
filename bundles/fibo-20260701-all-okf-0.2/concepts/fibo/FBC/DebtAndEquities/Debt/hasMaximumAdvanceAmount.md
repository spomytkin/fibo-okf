---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has maximum advance amount
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the ceiling on the amount of credit that can be drawn by the borrower in a single request with respect
      to a specific agreement (e.g. for line of credit) within the specified credit limit
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaximumAdvanceAmount
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has maximum advance amount
type: Ontology Property
---

# has maximum advance amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasMaximumAdvanceAmount>

## Definition

specifies the ceiling on the amount of credit that can be drawn by the borrower in a single request with respect to a specific agreement (e.g. for line of credit) within the specified credit limit

## Relationships

- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has maximum advance amount
- **definition**: specifies the ceiling on the amount of credit that can be drawn by the borrower in a single request with respect to a specific agreement (e.g. for line of credit) within the specified credit limit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
