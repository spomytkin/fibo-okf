---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: guaranteed loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan that is secured with respect to repayment of principal and interest by guaranty
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A loan guarantee is a promise by one party to assume the debt obligation of a borrower if that borrower defaults.
      A guarantee can be limited or unlimited, making the guarantor liable for only a portion or all of the debt.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the U.S., the term 'guaranteed loan' typically refers to a loan that is backed by a federal agency, such as
      the Department of Veterans Affairs or the Small Business Administration. Student loans may be guaranteed by the Student
      Loan Marketing Association.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantor
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/SecuredLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/GuaranteedLoan
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: guaranteed loan
type: Ontology Class
---

# guaranteed loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/GuaranteedLoan>

## Definition

loan that is secured with respect to repayment of principal and interest by guaranty

## Relationships

- **Subclass of**: [SecuredLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/SecuredLoan.md)

## Constraints

- **[hasGuarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasGuarantor.md)**: some values from of type [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md)

## Annotations

- **label** (en): guaranteed loan
- **definition** (en): loan that is secured with respect to repayment of principal and interest by guaranty
- **explanatoryNote** (en): A loan guarantee is a promise by one party to assume the debt obligation of a borrower if that borrower defaults. A guarantee can be limited or unlimited, making the guarantor liable for only a portion or all of the debt.
- **explanatoryNote** (en): In the U.S., the term 'guaranteed loan' typically refers to a loan that is backed by a federal agency, such as the Department of Veterans Affairs or the Small Business Administration. Student loans may be guaranteed by the Student Loan Marketing Association.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
