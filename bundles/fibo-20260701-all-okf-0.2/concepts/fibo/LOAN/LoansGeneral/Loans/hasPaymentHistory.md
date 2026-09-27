---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has payment history
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a credit agreement, loan, or commitment to any history of payments that have been made by the borrower
      up to the point that payment history is requested
  range:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/PaymentHistory.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Documents/hasRecord.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasRecord
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPaymentHistory
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has payment history
type: Ontology Property
---

# has payment history

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasPaymentHistory>

## Definition

relates a credit agreement, loan, or commitment to any history of payments that have been made by the borrower up to the point that payment history is requested

## Relationships

- **Range**: [PaymentHistory](/concepts/fibo/LOAN/LoansGeneral/Loans/PaymentHistory.md)
- **Subproperty of**: [hasRecord](/concepts/fibo/FND/Arrangements/Documents/hasRecord.md)

## Annotations

- **label**: has payment history
- **definition**: relates a credit agreement, loan, or commitment to any history of payments that have been made by the borrower up to the point that payment history is requested

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
