---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial securities secondary market transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A Transaction in which some negotiable security is provided in exchange for some Consideration.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionCounterparty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionPrincipal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/consideration
    value: N23c1762024c14eee8452eaa9a3267ddd
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/subject
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/embodies
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransaction
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction
sources:
- id: fibo-source-b8d1f073c7
  resource: references/fibo/FND/TransactionsExt/SecuritiesTransactions.rdf
  sha256: b8d1f073c7f5a249c4aca92393d0d5fbb1100d1d19fc7977632a0f8643da347d
  title: FIBO source FND/TransactionsExt/SecuritiesTransactions.rdf
title: financial securities secondary market transaction
type: Ontology Class
---

# financial securities secondary market transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction>

## Definition

A Transaction in which some negotiable security is provided in exchange for some Consideration.

## Relationships

- **Subclass of**: [MarketTransaction](/concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransaction.md)
- **Subclass of**: [ContractualTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/ContractualTransaction.md)

## Constraints

- **[hasCounterparty](/concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md)**: some values from of type [SecuritiesTransactionCounterparty](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionCounterparty.md)
- **[hasPrincipalParty](/concepts/fibo/FND/Agreements/Contracts/hasPrincipalParty.md)**: some values from of type [SecuritiesTransactionPrincipal](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionPrincipal.md)
- **[consideration](/concepts/fibo/FND/TransactionsExt/MarketTransactions/consideration.md)**: some values from value `N23c1762024c14eee8452eaa9a3267ddd`
- **[subject](/concepts/fibo/FND/TransactionsExt/REATransactions/subject.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[embodies](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/embodies.md)**: some values from of type [SecuritiesTransactionContract](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract.md)

## Annotations

- **label** (en): financial securities secondary market transaction
- **definition** (en): A Transaction in which some negotiable security is provided in exchange for some Consideration.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
