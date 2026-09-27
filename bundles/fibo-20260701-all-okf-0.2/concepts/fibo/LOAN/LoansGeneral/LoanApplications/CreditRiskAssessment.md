---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit risk assessment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: risk assessment that focuses on determining the likelihood of a potential borrower repaying a loan
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: If the risk assessment is based on one of the automated underwriting sytems, then the underwriting automation category
      is 'automated'. This dependency could be automated (as it were).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReport
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalContract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecord
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/UnderwritingDecision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasOutput
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/usesFactor
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/usesFactor
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/usesFactor
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/usesFactor
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentActivity
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/CreditRiskAssessment
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: credit risk assessment
type: Ontology Class
---

# credit risk assessment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/CreditRiskAssessment>

## Definition

risk assessment that focuses on determining the likelihood of a potential borrower repaying a loan

## Relationships

- **Subclass of**: [AssessmentActivity](/concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md)

## Constraints

- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [CreditReport](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/CreditReport.md)
- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [PreApprovalContract](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/PreApprovalContract.md)
- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [PreApprovalRequest](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest.md)
- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [PublicRecord](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/PublicRecord.md)
- **[hasOutput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasOutput.md)**: some values from of type [UnderwritingDecision](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/UnderwritingDecision.md)
- **[usesFactor](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/usesFactor.md)**: some values from of type [AllBorrowersMonthlyIncome](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/AllBorrowersMonthlyIncome.md)
- **[usesFactor](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/usesFactor.md)**: some values from of type [BorrowerMonthlyIncome](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome.md)
- **[usesFactor](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/usesFactor.md)**: some values from of type [TotalDebtExpenseRatio](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio.md)
- **[usesFactor](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/usesFactor.md)**: some values from of type [CombinedLoanToValueRatio](/concepts/fibo/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Annotations

- **label**: credit risk assessment
- **definition**: risk assessment that focuses on determining the likelihood of a potential borrower repaying a loan
- **usageNote**: If the risk assessment is based on one of the automated underwriting sytems, then the underwriting automation category is 'automated'. This dependency could be automated (as it were).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
