---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: payment terms
  domain:
  - concept: /concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransaction
  range:
  - concept: /concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/transactedUnder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactedUnder
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/paymentTerms
sources:
- id: fibo-source-c6db657dd3
  resource: references/fibo/FND/TransactionsExt/MarketTransactions.rdf
  sha256: c6db657dd322bad9135c79dfe7fe0e80f7e2c5aaff92ca4b48c056a156ccc943
  title: FIBO source FND/TransactionsExt/MarketTransactions.rdf
title: payment terms
type: Ontology Property
---

# payment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/paymentTerms>

## Relationships

- **Domain**: [MarketTransaction](/concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransaction.md)
- **Range**: [MarketTransactionPaymentTerms](/concepts/fibo/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms.md)
- **Subproperty of**: [transactedUnder](/concepts/fibo/FND/TransactionsExt/REATransactions/transactedUnder.md)

## Annotations

- **label** (en): payment terms

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
