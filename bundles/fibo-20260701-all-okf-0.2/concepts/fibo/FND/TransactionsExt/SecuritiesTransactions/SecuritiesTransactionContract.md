---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities transaction contract
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The contract (written or implied) which governs the transaction of securities in the secondary Market.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This is in line with the REA Ontology in which all Transactions are embodied in some Contract, whether written
      or implied. forms part of future "Transaction" model to be reviewed, but is ancestral to Options contract and transactions
      model.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/governs
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract
sources:
- id: fibo-source-b8d1f073c7
  resource: references/fibo/FND/TransactionsExt/SecuritiesTransactions.rdf
  sha256: b8d1f073c7f5a249c4aca92393d0d5fbb1100d1d19fc7977632a0f8643da347d
  title: FIBO source FND/TransactionsExt/SecuritiesTransactions.rdf
title: securities transaction contract
type: Ontology Class
---

# securities transaction contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract>

## Definition

The contract (written or implied) which governs the transaction of securities in the secondary Market.

## Relationships

- **Subclass of**: [EconomicContract](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicContract.md)

## Constraints

- **[governs](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/governs.md)**: some values from of type [FinancialSecuritiesSecondaryMarketTransaction](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction.md)

## Annotations

- **label** (en): securities transaction contract
- **definition** (en): The contract (written or implied) which governs the transaction of securities in the secondary Market.
- **editorialNote** (en): This is in line with the REA Ontology in which all Transactions are embodied in some Contract, whether written or implied. forms part of future "Transaction" model to be reviewed, but is ancestral to Options contract and transactions model.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
