---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual transaction
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An economic transaction which has some contractual basis.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is distinct from a transaction between business units within an enterprise. This is the usual sense of "Transaction"
      and forms the basis for all securities and derivatives transactions, while the parent term "Economic Transaction" may
      also be used to define internal transactions and transactions that have no legal or contractual basis.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransaction
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: contractual transaction
type: Ontology Class
---

# contractual transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransaction>

## Definition

An economic transaction which has some contractual basis.

## Relationships

- **Subclass of**: [EconomicTransaction](/concepts/fibo/FND/TransactionsExt/REATransactions/EconomicTransaction.md)

## Annotations

- **label** (en): contractual transaction
- **definition** (en): An economic transaction which has some contractual basis.
- **explanatoryNote** (en): This is distinct from a transaction between business units within an enterprise. This is the usual sense of "Transaction" and forms the basis for all securities and derivatives transactions, while the parent term "Economic Transaction" may also be used to define internal transactions and transactions that have no legal or contractual basis.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
