---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: borrowing capacity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: upper bound on the total amount of money that a lender believes a party has the ability to repay an obligation
      when due, as of some point in time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The notion of borrowing capacity is related to management decisions pertaining to credit, i.e., the creditworthiness
      of the borrower, loan amount, risk tolerance, and so forth, and may be reassessed from time to time depending on the
      type of credit agreement and regulatory requirements. Determining borrowing capacity is typically done as a part of
      loan origination, especially for residential mortgages.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentReport
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/hasDateOfAssessment
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowingCapacity
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: borrowing capacity
type: Ontology Class
---

# borrowing capacity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowingCapacity>

## Definition

upper bound on the total amount of money that a lender believes a party has the ability to repay an obligation when due, as of some point in time

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: some values from of type [AssessmentReport](/concepts/fibo/FND/Arrangements/Assessments/AssessmentReport.md)
- **[hasDateOfAssessment](/concepts/fibo/FND/Arrangements/Assessments/hasDateOfAssessment.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Annotations

- **label**: borrowing capacity
- **definition**: upper bound on the total amount of money that a lender believes a party has the ability to repay an obligation when due, as of some point in time
- **explanatoryNote**: The notion of borrowing capacity is related to management decisions pertaining to credit, i.e., the creditworthiness of the borrower, loan amount, risk tolerance, and so forth, and may be reassessed from time to time depending on the type of credit agreement and regulatory requirements. Determining borrowing capacity is typically done as a part of loan origination, especially for residential mortgages.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
