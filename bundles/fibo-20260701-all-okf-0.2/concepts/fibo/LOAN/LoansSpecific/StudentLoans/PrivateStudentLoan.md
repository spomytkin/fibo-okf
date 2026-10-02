---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private student loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: student loan that is not considered a government-backed / regulated loan
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/StudentLoans/RegulatedStudentLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/RegulatedStudentLoan
  - concept: /concepts/fibo/LOAN/LoansSpecific/StudentLoans/StudentLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/StudentLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/PrivateStudentLoan
sources:
- id: fibo-source-2e024d7951
  resource: references/fibo/LOAN/LoansSpecific/StudentLoans.rdf
  sha256: 2e024d79512aeb643d4e0bfd2473cf6fb5ed3cf7fa306e0abcd66d66fdcc0d68
  title: FIBO source LOAN/LoansSpecific/StudentLoans.rdf
title: private student loan
type: Ontology Class
---

# private student loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/PrivateStudentLoan>

## Definition

student loan that is not considered a government-backed / regulated loan

## Relationships

- **Subclass of**: [RegulatedStudentLoan](/concepts/fibo/LOAN/LoansSpecific/StudentLoans/RegulatedStudentLoan.md)
- **Subclass of**: [StudentLoan](/concepts/fibo/LOAN/LoansSpecific/StudentLoans/StudentLoan.md)

## Annotations

- **label** (en): private student loan
- **definition** (en): student loan that is not considered a government-backed / regulated loan

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
