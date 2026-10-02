---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has maximum allowed balance
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: maximum balance that may be outstanding at any time, below the credit limit, for loans with flexible re-draw facilities
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
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/hasMaximumAllowedBalance
sources:
- id: fibo-source-c8807a0349
  resource: references/fibo/LOAN/RealEstateLoans/ConstructionLoans.rdf
  sha256: c8807a0349286758472a44895c182ef590265f17f0b2af37b0bdae6d5c206f68
  title: FIBO source LOAN/RealEstateLoans/ConstructionLoans.rdf
title: has maximum allowed balance
type: Ontology Property
---

# has maximum allowed balance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/hasMaximumAllowedBalance>

## Definition

maximum balance that may be outstanding at any time, below the credit limit, for loans with flexible re-draw facilities

## Relationships

- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasAvailableAmount](/concepts/fibo/FBC/DebtAndEquities/Debt/hasAvailableAmount.md)

## Annotations

- **label** (en): has maximum allowed balance
- **definition** (en): maximum balance that may be outstanding at any time, below the credit limit, for loans with flexible re-draw facilities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
