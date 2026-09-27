---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: student loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan provided for the purposes of education, allowing students and parents/guardians to borrow money for college
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Student loans may include loans for graduate and professional education. Student loans may be obtained from government
      institutions, from private sources such as a bank or financial institution, or from other organizations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
    value: Nb46113dd33ae4addb8503812a4ec9442
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/StudentLoan
sources:
- id: fibo-source-2e024d7951
  resource: references/fibo/LOAN/LoansSpecific/StudentLoans.rdf
  sha256: 2e024d79512aeb643d4e0bfd2473cf6fb5ed3cf7fa306e0abcd66d66fdcc0d68
  title: FIBO source LOAN/LoansSpecific/StudentLoans.rdf
title: student loan
type: Ontology Class
---

# student loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/StudentLoan>

## Definition

loan provided for the purposes of education, allowing students and parents/guardians to borrow money for college

## Relationships

- **Subclass of**: [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from value `Nb46113dd33ae4addb8503812a4ec9442`

## Annotations

- **label** (en): student loan
- **definition** (en): loan provided for the purposes of education, allowing students and parents/guardians to borrow money for college
- **explanatoryNote** (en): Student loans may include loans for graduate and professional education. Student loans may be obtained from government institutions, from private sources such as a bank or financial institution, or from other organizations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
