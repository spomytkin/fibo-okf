---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: individual payment transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: actual payment of principal, interest, fees, or other related amounts towards fulfillment of a debt obligation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: individual payment transaction
type: Ontology Class
---

# individual payment transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/IndividualPaymentTransaction>

## Definition

actual payment of principal, interest, fees, or other related amounts towards fulfillment of a debt obligation

## Relationships

- **Subclass of**: [IndividualTransaction](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md)
- **Subclass of**: [Payment](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/Payment.md)

## Annotations

- **label** (en): individual payment transaction
- **definition** (en): actual payment of principal, interest, fees, or other related amounts towards fulfillment of a debt obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
