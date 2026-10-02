---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: open-end credit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period
      of the line, if any, and on which interest is charged only on the outstanding balance
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Credit card and overdraft lines of credit are among the most widely used forms of open-end credit.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There is a credit limit most of the time, with exceptions including reverse mortgages with tenure payment. The
      borrower has the option of paying off the outstanding balance, without penalty, or making installment payments.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: charge account credit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: revolving credit
  disjoint_with:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/ClosedEndCredit.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/ClosedEndCredit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasCreditLimit
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OpenEndCredit
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: open-end credit
type: Ontology Class
---

# open-end credit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OpenEndCredit>

## Definition

credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period of the line, if any, and on which interest is charged only on the outstanding balance

## Relationships

- **Subclass of**: [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)

## Constraints

- **Disjoint with**: [ClosedEndCredit](/concepts/fibo/LOAN/LoansGeneral/Loans/ClosedEndCredit.md)
- **[hasCreditLimit](/concepts/fibo/FBC/DebtAndEquities/Debt/hasCreditLimit.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: open-end credit
- **definition**: credit agreement that may be extended up to an agreed credit limit and paid down at any time within the period of the line, if any, and on which interest is charged only on the outstanding balance
- **example**: Credit card and overdraft lines of credit are among the most widely used forms of open-end credit.
- **explanatoryNote**: There is a credit limit most of the time, with exceptions including reverse mortgages with tenure payment. The borrower has the option of paying off the outstanding balance, without penalty, or making installment payments.
- **synonym**: charge account credit
- **synonym**: revolving credit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
