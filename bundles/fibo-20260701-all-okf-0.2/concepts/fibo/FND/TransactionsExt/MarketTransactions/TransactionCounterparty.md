---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction counterparty
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Counterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionCounterparty
sources:
- id: fibo-source-c6db657dd3
  resource: references/fibo/FND/TransactionsExt/MarketTransactions.rdf
  sha256: c6db657dd322bad9135c79dfe7fe0e80f7e2c5aaff92ca4b48c056a156ccc943
  title: FIBO source FND/TransactionsExt/MarketTransactions.rdf
title: transaction counterparty
type: Ontology Class
---

# transaction counterparty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionCounterparty>

## Relationships

- **Subclass of**: [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)
- **Subclass of**: [TransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md)

## Annotations

- **label** (en): transaction counterparty

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
