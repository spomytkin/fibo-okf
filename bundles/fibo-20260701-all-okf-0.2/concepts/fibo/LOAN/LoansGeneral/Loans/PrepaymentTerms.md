---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pre-payment terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: principal repayment terms related to payment of the loan prior to maturity
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Prepayment may or may not involve refinancing with the same lender. Prepayment terms include any prepayment penalty
      period, penalty amount and whether or not there is provision for waiver of the penalty, and any conditions related to
      making additional payments or payments over and above the expected installment payment over the lifetime of the loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPrePaymentPenaltyTerm
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PrepaymentTerms
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: pre-payment terms
type: Ontology Class
---

# pre-payment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PrepaymentTerms>

## Definition

principal repayment terms related to payment of the loan prior to maturity

## Relationships

- **Subclass of**: [PrincipalRepaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)

## Constraints

- **[hasPrePaymentPenaltyTerm](/concepts/fibo/LOAN/LoansGeneral/Loans/hasPrePaymentPenaltyTerm.md)**: some values from of type [ExplicitDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDuration>)

## Annotations

- **label** (en): pre-payment terms
- **definition** (en): principal repayment terms related to payment of the loan prior to maturity
- **explanatoryNote** (en): Prepayment may or may not involve refinancing with the same lender. Prepayment terms include any prepayment penalty period, penalty amount and whether or not there is provision for waiver of the penalty, and any conditions related to making additional payments or payments over and above the expected installment payment over the lifetime of the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
