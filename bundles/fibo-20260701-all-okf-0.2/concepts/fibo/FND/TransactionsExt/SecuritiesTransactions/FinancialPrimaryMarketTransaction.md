---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial primary market transaction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/follows
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransaction
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction
sources:
- id: fibo-source-b8d1f073c7
  resource: references/fibo/FND/TransactionsExt/SecuritiesTransactions.rdf
  sha256: b8d1f073c7f5a249c4aca92393d0d5fbb1100d1d19fc7977632a0f8643da347d
  title: FIBO source FND/TransactionsExt/SecuritiesTransactions.rdf
title: financial primary market transaction
type: Ontology Class
---

# financial primary market transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction>

## Relationships

- **Subclass of**: [MarketTransaction](/concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransaction.md)
- **Subclass of**: [ContractualTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransaction.md)

## Constraints

- **[follows](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/follows.md)**: some values from of type [SettlementProcess](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess.md)

## Annotations

- **label** (en): financial primary market transaction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
