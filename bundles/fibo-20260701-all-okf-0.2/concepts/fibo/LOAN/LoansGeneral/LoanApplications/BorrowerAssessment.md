---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: borrower assessment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assessment report detailing information about the borrower and their credit history that may be relevant to the
      loan application
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Includes credit rating information. Ongoing assessment reports both good and bad credit rating information. In
      the US, by regulation, lender is required to respot person's payment history on a monthly basis. This is the basis on
      which peope's score is changed. So the lender's reporting to the credit bureau may affect that person's credit rating.
      this may give rise to credit disputes. Also there is a scenario where the borrower may contact the lender and ask for
      some change. For student loans, they can apply for a deferment payment based on change in circumstances e.g. if losing
      job, or becoming disabled, then there are specific programs which they can apply for. can defer paymen for a time, and
      if proven eligible (e.g. also if in military, being deployed), then if they subbut the relevant document, they approve
      and change their repayment term, perhaps temporarily and then revert to the previously agreed terms. This results from
      the borrower contacting the lender.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasDateOfAssessment
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IndividualPersonCreditRating
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: borrower assessment
type: Ontology Class
---

# borrower assessment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment>

## Definition

assessment report detailing information about the borrower and their credit history that may be relevant to the loan application

## Relationships

- **Subclass of**: [AssessmentReport](/concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md)

## Constraints

- **[hasDateOfAssessment](/concepts/fibo/FND/Arrangements/Assessments/hasDateOfAssessment.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [IncomeVerificationReport](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [IndividualPersonCreditRating](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/IndividualPersonCreditRating.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [PaymentHistory](/concepts/fibo/LOAN/LoansGeneral/Loans/PaymentHistory.md)
- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [Borrower](/concepts/fibo/FBC/DebtAndEquities/Debt/Borrower.md)
- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [LoanApplication](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md)

## Annotations

- **label** (en): borrower assessment
- **definition** (en): assessment report detailing information about the borrower and their credit history that may be relevant to the loan application
- **explanatoryNote** (en): Includes credit rating information. Ongoing assessment reports both good and bad credit rating information. In the US, by regulation, lender is required to respot person's payment history on a monthly basis. This is the basis on which peope's score is changed. So the lender's reporting to the credit bureau may affect that person's credit rating. this may give rise to credit disputes. Also there is a scenario where the borrower may contact the lender and ask for some change. For student loans, they can apply for a deferment payment based on change in circumstances e.g. if losing job, or becoming disabled, then there are specific programs which they can apply for. can defer paymen for a time, and if proven eligible (e.g. also if in military, being deployed), then if they subbut the relevant document, they approve and change their repayment term, perhaps temporarily and then revert to the previously agreed terms. This results from the borrower contacting the lender.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
