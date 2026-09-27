---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has milestone maximum drawdown amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: maximum amount of the loan that can be drawn by the borrower on completion of the milestone
  domain:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/hasAvailableAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAvailableAmount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/hasMilestoneMaximumDrawdownAmount
sources:
- id: fibo-source-c8807a0349
  resource: references/fibo/LOAN/RealEstateLoans/ConstructionLoans.rdf
  sha256: c8807a0349286758472a44895c182ef590265f17f0b2af37b0bdae6d5c206f68
  title: FIBO source LOAN/RealEstateLoans/ConstructionLoans.rdf
title: has milestone maximum drawdown amount
type: Ontology Property
---

# has milestone maximum drawdown amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/hasMilestoneMaximumDrawdownAmount>

## Definition

maximum amount of the loan that can be drawn by the borrower on completion of the milestone

## Relationships

- **Domain**: [ContractMilestone](/concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasAvailableAmount](/concepts/fibo/FBC/DebtAndEquities/Debt/hasAvailableAmount.md)

## Annotations

- **label** (en): has milestone maximum drawdown amount
- **definition** (en): maximum amount of the loan that can be drawn by the borrower on completion of the milestone

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
