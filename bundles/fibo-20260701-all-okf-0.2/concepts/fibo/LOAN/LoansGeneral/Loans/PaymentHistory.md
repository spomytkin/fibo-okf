---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment history
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: record of actual payments of principal, interest, and other related amounts made by a borrower to a lender or servicer
      in order to fulfill their re-payment obligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasIndividualPayment
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: payment history
type: Ontology Class
---

# payment history

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory>

## Definition

record of actual payments of principal, interest, and other related amounts made by a borrower to a lender or servicer in order to fulfill their re-payment obligation

## Relationships

- **Subclass of**: [TransactionRecord](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)

## Constraints

- **[appliesToAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount.md)**: some values from of type [LoanSpecificCustomerAccount](/concepts/fibo/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md)
- **[hasIndividualPayment](/concepts/fibo/LOAN/LoansGeneral/Loans/hasIndividualPayment.md)**: some values from of type [IndividualPaymentTransaction](/concepts/fibo/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction.md)

## Annotations

- **label**: payment history
- **definition**: record of actual payments of principal, interest, and other related amounts made by a borrower to a lender or servicer in order to fulfill their re-payment obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
