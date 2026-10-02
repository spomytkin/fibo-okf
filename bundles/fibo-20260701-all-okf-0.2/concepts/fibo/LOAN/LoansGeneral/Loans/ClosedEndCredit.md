---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: closed-end credit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement in which the loan principal cannot be increased after funds are dispersed in full when the loan
      closes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The loan may require regular payments that pay down principal periodically, or it may require the full payment
      of principal at maturity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/ClosedEndCredit
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: closed-end credit
type: Ontology Class
---

# closed-end credit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/ClosedEndCredit>

## Definition

credit agreement in which the loan principal cannot be increased after funds are dispersed in full when the loan closes

## Relationships

- **Subclass of**: [CreditAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreement.md)

## Annotations

- **label**: closed-end credit
- **definition**: credit agreement in which the loan principal cannot be increased after funds are dispersed in full when the loan closes
- **explanatoryNote**: The loan may require regular payments that pay down principal periodically, or it may require the full payment of principal at maturity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
