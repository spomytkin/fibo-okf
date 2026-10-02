---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has original loan debt-to-income ratio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the debt-to-income (DTI) ratio at the time when the loan was advanced; for combined income
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasOriginalLoanDebtToIncomeRatio
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: has original loan debt-to-income ratio
type: Ontology Property
---

# has original loan debt-to-income ratio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasOriginalLoanDebtToIncomeRatio>

## Definition

indicates the debt-to-income (DTI) ratio at the time when the loan was advanced; for combined income

## Relationships

- **Domain**: [BorrowerAssessment](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md)
- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label** (en): has original loan debt-to-income ratio
- **definition** (en): indicates the debt-to-income (DTI) ratio at the time when the loan was advanced; for combined income

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
