---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has gross income
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the personal gross income of the borrower
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasGrossIncome
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: has gross income
type: Ontology Property
---

# has gross income

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasGrossIncome>

## Definition

indicates the personal gross income of the borrower

## Relationships

- **Domain**: [BorrowerAssessment](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label** (en): has gross income
- **definition** (en): indicates the personal gross income of the borrower

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
