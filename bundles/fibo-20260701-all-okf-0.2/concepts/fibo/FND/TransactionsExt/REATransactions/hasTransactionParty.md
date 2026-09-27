---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has transaction party
  domain:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
  range:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/hasTransactionParty
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: has transaction party
type: Ontology Property
---

# has transaction party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/hasTransactionParty>

## Relationships

- **Domain**: [EconomicTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md)
- **Range**: [TransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md)

## Annotations

- **label** (en): has transaction party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
