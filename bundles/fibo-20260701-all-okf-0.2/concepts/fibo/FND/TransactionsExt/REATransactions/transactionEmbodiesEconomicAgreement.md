---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction embodies economic agreement
  domain:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
  inverse_of:
  - predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  range:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicAgreement
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactionEmbodiesEconomicAgreement
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: transaction embodies economic agreement
type: Ontology Property
---

# transaction embodies economic agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/transactionEmbodiesEconomicAgreement>

## Relationships

- **Domain**: [EconomicTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md)
- **Inverse of**: [governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)
- **Range**: [EconomicAgreement](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicAgreement.md)

## Annotations

- **label** (en): transaction embodies economic agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
