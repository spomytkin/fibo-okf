---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan application
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: request by a potential borrower to a potential lender to borrow money containing information used to decide whether
      to grant the loan
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: The request typicaly includes most, if not all, of the information used to decide whether to grant the loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Requester
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedBy
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasDateReceived
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasApplicationDate
  - filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/isPreApprovalRequested
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanToValueRatio
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Document
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: loan application
type: Ontology Class
---

# loan application

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication>

## Definition

request by a potential borrower to a potential lender to borrow money containing information used to decide whether to grant the loan

## Relationships

- **Subclass of**: [Document](<https://www.omg.org/spec/Commons/Documents/Document>)

## Constraints

- **[isSubmittedBy](/concepts/fibo/FND/Arrangements/Reporting/isSubmittedBy.md)**: some values from of type [Requester](/concepts/fibo/FND/Arrangements/Reporting/Requester.md)
- **[hasDateReceived](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasDateReceived.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasApplicationDate](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/hasApplicationDate.md)**: exact qualified cardinality 1 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[isPreApprovalRequested](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/isPreApprovalRequested.md)**: some values from of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [CombinedLoanToValueRatio](/concepts/fibo/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [LoanToValueRatio](/concepts/fibo/LOAN/LoansGeneral/Loans/LoanToValueRatio.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [AllBorrowersMonthlyIncome](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [BorrowerMonthlyIncome](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [TotalDebtExpenseRatio](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio.md)

## Annotations

- **label**: loan application
- **definition**: request by a potential borrower to a potential lender to borrow money containing information used to decide whether to grant the loan
- **scopeNote**: The request typicaly includes most, if not all, of the information used to decide whether to grant the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
