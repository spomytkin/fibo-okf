---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has scheduled unpaid balance
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates what the balance should be after a scheduled payment is made according to contract terms
  range:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasScheduledUnpaidBalance
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: has scheduled unpaid balance
type: Ontology Property
---

# has scheduled unpaid balance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/hasScheduledUnpaidBalance>

## Definition

indicates what the balance should be after a scheduled payment is made according to contract terms

## Relationships

- **Range**: [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **Subproperty of**: [hasBalance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md)

## Annotations

- **label**: has scheduled unpaid balance
- **definition**: indicates what the balance should be after a scheduled payment is made according to contract terms

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
