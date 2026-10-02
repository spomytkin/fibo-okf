---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regulated student loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: student loan (1) whose lender is a government agency or instrumentality, and/or (2) that is treated uniquely due
      to tax regulations
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, certain student loans survive bankruptcy and are subject to additional tax regulations that
      do not apply to other kinds of loans.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/StudentLoans/StudentLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/StudentLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/RegulatedStudentLoan
sources:
- id: fibo-source-2e024d7951
  resource: references/fibo/LOAN/LoansSpecific/StudentLoans.rdf
  sha256: 2e024d79512aeb643d4e0bfd2473cf6fb5ed3cf7fa306e0abcd66d66fdcc0d68
  title: FIBO source LOAN/LoansSpecific/StudentLoans.rdf
title: regulated student loan
type: Ontology Class
---

# regulated student loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/StudentLoans/RegulatedStudentLoan>

## Definition

student loan (1) whose lender is a government agency or instrumentality, and/or (2) that is treated uniquely due to tax regulations

## Relationships

- **Subclass of**: [StudentLoan](/concepts/fibo/LOAN/LoansSpecific/StudentLoans/StudentLoan.md)

## Annotations

- **label** (en): regulated student loan
- **definition** (en): student loan (1) whose lender is a government agency or instrumentality, and/or (2) that is treated uniquely due to tax regulations
- **explanatoryNote** (en): In the United States, certain student loans survive bankruptcy and are subject to additional tax regulations that do not apply to other kinds of loans.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
