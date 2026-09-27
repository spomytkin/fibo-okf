---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: governs
  domain:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract
  inverse_of:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/embodies.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/embodies
  range:
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/governs
sources:
- id: fibo-source-b8d1f073c7
  resource: references/fibo/FND/TransactionsExt/SecuritiesTransactions.rdf
  sha256: b8d1f073c7f5a249c4aca92393d0d5fbb1100d1d19fc7977632a0f8643da347d
  title: FIBO source FND/TransactionsExt/SecuritiesTransactions.rdf
title: governs
type: Ontology Property
---

# governs

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/governs>

## Relationships

- **Domain**: [SecuritiesTransactionContract](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract.md)
- **Inverse of**: [embodies](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/embodies.md)
- **Range**: [FinancialSecuritiesSecondaryMarketTransaction](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction.md)
- **Subproperty of**: [governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)

## Annotations

- **label** (en): governs

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
