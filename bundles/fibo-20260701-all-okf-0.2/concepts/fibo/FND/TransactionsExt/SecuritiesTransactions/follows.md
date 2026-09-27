---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: follows
  domain:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction
  range:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/transactionEventFollowsBusinessProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactionEventFollowsBusinessProcess
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/follows
sources:
- id: fibo-source-b8d1f073c7
  resource: references/fibo/FND/TransactionsExt/SecuritiesTransactions.rdf
  sha256: b8d1f073c7f5a249c4aca92393d0d5fbb1100d1d19fc7977632a0f8643da347d
  title: FIBO source FND/TransactionsExt/SecuritiesTransactions.rdf
title: follows
type: Ontology Property
---

# follows

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/follows>

## Relationships

- **Domain**: [FinancialPrimaryMarketTransaction](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction.md)
- **Range**: [SettlementProcess](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess.md)
- **Subproperty of**: [transactionEventFollowsBusinessProcess](/concepts/fibo/FND/TransactionsExt/REATransactions/transactionEventFollowsBusinessProcess.md)

## Annotations

- **label** (en): follows

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
