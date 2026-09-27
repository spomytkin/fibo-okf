---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has amount of credit extended
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the gross amount of credit that has been provided to the borrower as of a given point in time with respect
      to a specific agreement (e.g. for line of credit)
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAmountOfCreditExtended
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has amount of credit extended
type: Ontology Property
---

# has amount of credit extended

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAmountOfCreditExtended>

## Definition

specifies the gross amount of credit that has been provided to the borrower as of a given point in time with respect to a specific agreement (e.g. for line of credit)

## Relationships

- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label**: has amount of credit extended
- **definition**: specifies the gross amount of credit that has been provided to the borrower as of a given point in time with respect to a specific agreement (e.g. for line of credit)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
