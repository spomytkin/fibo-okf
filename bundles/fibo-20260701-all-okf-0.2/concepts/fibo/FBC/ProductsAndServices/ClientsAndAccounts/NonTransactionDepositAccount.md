---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-transaction deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any deposit account that is not explicitly considered a transaction account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Non-transaction accounts include: (a) savings deposits ((i) money market deposit accounts (MMDAs) and (ii) other
      savings deposits) and (b) time deposits ((i) time certificates of deposit and (ii) time deposits, open account).'
  disjoint_with:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: non-transaction deposit account
type: Ontology Class
---

# non-transaction deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount>

## Definition

any deposit account that is not explicitly considered a transaction account

## Relationships

- **Subclass of**: [DepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md)

## Constraints

- **Disjoint with**: [TransactionDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount.md)

## Annotations

- **label**: non-transaction deposit account
- **definition**: any deposit account that is not explicitly considered a transaction account
- **explanatoryNote**: Non-transaction accounts include: (a) savings deposits ((i) money market deposit accounts (MMDAs) and (ii) other savings deposits) and (b) time deposits ((i) time certificates of deposit and (ii) time deposits, open account).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
