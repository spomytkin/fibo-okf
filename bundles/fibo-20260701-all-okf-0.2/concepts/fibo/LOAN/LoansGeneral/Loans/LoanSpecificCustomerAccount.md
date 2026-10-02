---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan-specific customer account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account held by the borrower associated with a specific loan
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanPaymentSchedule
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasLoanBalance
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPaymentHistory
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
    value: N89c2338519724116a666032f07e3b71f
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: loan-specific customer account
type: Ontology Class
---

# loan-specific customer account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount>

## Definition

account held by the borrower associated with a specific loan

## Relationships

- **Subclass of**: [CustomerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- **Subclass of**: [LoanOrCreditAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)

## Constraints

- **[relatesTo](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/relatesTo.md)**: some values from of type [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)
- **[hasPaymentSchedule](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/hasPaymentSchedule.md)**: min qualified cardinality 0 of type [LoanPaymentSchedule](/concepts/fibo/LOAN/LoansGeneral/Loans/LoanPaymentSchedule.md)
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: some values from of type [Borrower](/concepts/fibo/FBC/DebtAndEquities/Debt/Borrower.md)
- **[hasLoanBalance](/concepts/fibo/LOAN/LoansGeneral/Loans/hasLoanBalance.md)**: min qualified cardinality 0 of type [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **[hasPaymentHistory](/concepts/fibo/LOAN/LoansGeneral/Loans/hasPaymentHistory.md)**: min qualified cardinality 0 of type [PaymentHistory](/concepts/fibo/LOAN/LoansGeneral/Loans/PaymentHistory.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from value `N89c2338519724116a666032f07e3b71f`

## Annotations

- **label**: loan-specific customer account
- **definition**: account held by the borrower associated with a specific loan

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
