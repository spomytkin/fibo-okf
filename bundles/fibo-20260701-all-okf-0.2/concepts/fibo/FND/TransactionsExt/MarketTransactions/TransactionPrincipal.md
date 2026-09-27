---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction principal
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionCounterparty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactsWith
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionParty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionPrincipal
sources:
- id: fibo-source-c6db657dd3
  resource: references/fibo/FND/TransactionsExt/MarketTransactions.rdf
  sha256: c6db657dd322bad9135c79dfe7fe0e80f7e2c5aaff92ca4b48c056a156ccc943
  title: FIBO source FND/TransactionsExt/MarketTransactions.rdf
title: transaction principal
type: Ontology Class
---

# transaction principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionPrincipal>

## Relationships

- **Subclass of**: [ContractPrincipal](/concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md)
- **Subclass of**: [TransactionParty](/concepts/fibo/FND/TransactionsExt/REATransactions/TransactionParty.md)

## Constraints

- **[transactsWith](/concepts/fibo/FND/TransactionsExt/REATransactions/transactsWith.md)**: some values from of type [TransactionCounterparty](/concepts/fibo/FND/TransactionsExt/MarketTransactions/TransactionCounterparty.md)

## Annotations

- **label** (en): transaction principal

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
