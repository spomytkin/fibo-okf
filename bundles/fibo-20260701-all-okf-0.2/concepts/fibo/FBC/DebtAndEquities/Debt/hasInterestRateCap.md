---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has interest rate cap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something, such as an agreement, or debt instrument, to the upper bound (ceiling) rate (typically annual)
      of interest on variable-rate debt that is to be paid by the debtor to the creditor on the debt
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRateCap
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has interest rate cap
type: Ontology Property
---

# has interest rate cap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRateCap>

## Definition

relates something, such as an agreement, or debt instrument, to the upper bound (ceiling) rate (typically annual) of interest on variable-rate debt that is to be paid by the debtor to the creditor on the debt

## Relationships

- **Range**: [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **Subproperty of**: [hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)

## Annotations

- **label**: has interest rate cap
- **definition**: relates something, such as an agreement, or debt instrument, to the upper bound (ceiling) rate (typically annual) of interest on variable-rate debt that is to be paid by the debtor to the creditor on the debt

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
