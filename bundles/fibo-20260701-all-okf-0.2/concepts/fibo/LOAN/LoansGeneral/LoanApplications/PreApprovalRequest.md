---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pre-approval request
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: request from a potential borrower that a lender commit to pre-approving the borrower for a loan of up to a specified
      amount of money
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This may also include limits on the region where to purchase.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasRequestedAmount
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/RequestActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/RequestActivity
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: pre-approval request
type: Ontology Class
---

# pre-approval request

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest>

## Definition

request from a potential borrower that a lender commit to pre-approving the borrower for a loan of up to a specified amount of money

## Relationships

- **Subclass of**: [RequestActivity](/concepts/fibo/FND/Arrangements/Reporting/RequestActivity.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from of type [Borrower](/concepts/fibo/FBC/DebtAndEquities/Debt/Borrower.md)
- **[hasRequestedAmount](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/hasRequestedAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: pre-approval request
- **definition**: request from a potential borrower that a lender commit to pre-approving the borrower for a loan of up to a specified amount of money
- **explanatoryNote**: This may also include limits on the region where to purchase.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
