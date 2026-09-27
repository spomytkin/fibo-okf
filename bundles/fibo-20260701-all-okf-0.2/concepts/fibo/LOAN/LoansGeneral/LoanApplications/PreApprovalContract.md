---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pre-approval contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged
      creditworthiness
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A commitment from a lender to a borrower to extend a home purchase loan up to a certain amount, and subject to
      certain non-credit related conditions.  This commitment is entered into after a comprehensive analysis of the credit
      worthiness of the borrower is carried out.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This may also include limits on the region where to purchase.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasApprovedAmount
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalContract
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: pre-approval contract
type: Ontology Class
---

# pre-approval contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalContract>

## Definition

written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged creditworthiness

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasInterestRate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInterestRate.md)**: some values from of type [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **[hasApprovedAmount](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/hasApprovedAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: pre-approval contract
- **definition**: written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged creditworthiness
- **explanatoryNote**: A commitment from a lender to a borrower to extend a home purchase loan up to a certain amount, and subject to certain non-credit related conditions.  This commitment is entered into after a comprehensive analysis of the credit worthiness of the borrower is carried out.
- **explanatoryNote**: This may also include limits on the region where to purchase.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
