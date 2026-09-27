---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Any transaction which defines a supply of some negotiable item in return for some Consideration. The Market Transaction
      has a Principal and a Counterparty, i.e. it is not symmetrical.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionCounterparty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasCounterparty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionPrincipal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicResource
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/consideration
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/paymentTerms
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransaction
sources:
- id: fibo-source-c6db657dd3
  resource: references/fibo/FND/TransactionsExt/MarketTransactions.rdf
  sha256: c6db657dd322bad9135c79dfe7fe0e80f7e2c5aaff92ca4b48c056a156ccc943
  title: FIBO source FND/TransactionsExt/MarketTransactions.rdf
title: market transaction
type: Ontology Class
---

# market transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransaction>

## Definition

Any transaction which defines a supply of some negotiable item in return for some Consideration. The Market Transaction has a Principal and a Counterparty, i.e. it is not symmetrical.

## Relationships

- **Subclass of**: [EconomicTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md)

## Constraints

- **[hasCounterparty](/concepts/fibo/FND/Agreements/Contracts/hasCounterparty.md)**: some values from of type [TransactionCounterparty](/concepts/fibo/FND/TransactionsExt/MarketTransactions/TransactionCounterparty.md)
- **[hasPrincipalParty](/concepts/fibo/FND/Agreements/Contracts/hasPrincipalParty.md)**: some values from of type [TransactionPrincipal](/concepts/fibo/FND/TransactionsExt/MarketTransactions/TransactionPrincipal.md)
- **[consideration](/concepts/fibo/FND/TransactionsExt/MarketTransactions/consideration.md)**: some values from of type [EconomicResource](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicResource.md)
- **[paymentTerms](/concepts/fibo/FND/TransactionsExt/MarketTransactions/paymentTerms.md)**: some values from of type [MarketTransactionPaymentTerms](/concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms.md)

## Annotations

- **label** (en): market transaction
- **definition** (en): Any transaction which defines a supply of some negotiable item in return for some Consideration. The Market Transaction has a Principal and a Counterparty, i.e. it is not symmetrical.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
