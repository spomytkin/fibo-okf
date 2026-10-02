---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has individual payment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links an actual payment of principal, interest, and other related amounts to the overall payment history for an
      account
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/PaymentHistory.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
  range:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasIndividualPayment
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has individual payment
type: Ontology Property
---

# has individual payment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasIndividualPayment>

## Definition

links an actual payment of principal, interest, and other related amounts to the overall payment history for an account

## Relationships

- **Domain**: [PaymentHistory](/concepts/fibo/LOAN/LoansGeneral/Loans/PaymentHistory.md)
- **Range**: [IndividualPaymentTransaction](/concepts/fibo/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has individual payment
- **definition**: links an actual payment of principal, interest, and other related amounts to the overall payment history for an account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
