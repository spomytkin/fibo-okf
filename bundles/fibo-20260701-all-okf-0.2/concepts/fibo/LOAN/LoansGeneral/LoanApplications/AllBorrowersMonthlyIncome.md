---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: all borrowers' monthly income
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: total monthly qualifying income for all borrowers on the loan
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: This should be computed from the income of the individual borrowers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Income.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Income
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: all borrowers' monthly income
type: Ontology Class
---

# all borrowers' monthly income

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome>

## Definition

total monthly qualifying income for all borrowers on the loan

## Relationships

- **Subclass of**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subclass of**: [Income](/concepts/fibo/FND/OwnershipAndControl/Ownership/Income.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [BorrowerMonthlyIncome](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md)

## Annotations

- **label**: all borrowers' monthly income
- **definition**: total monthly qualifying income for all borrowers on the loan
- **usageNote**: This should be computed from the income of the individual borrowers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
