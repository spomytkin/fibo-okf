---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: deposit account from which the depositor / account holder is permitted to make transfers or withdrawals by negotiable
      / transferable instruments, payment orders of withdrawal, telephone transfers, and so forth, and that may be accessible
      via an electronic device such as an automated teller machine (ATM), remote service unit (RSU), mobile device, and by
      debit card
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Excluded from transaction accounts are savings deposits (both money market deposit accounts (MMDAs) and other savings
      deposits), even though such deposits permit some third-party transfers. However, an account that otherwise meets the
      definition of a savings deposit but that authorizes or permits the depositor to exceed the transfer limitations specified
      for that account shall be reported as a transaction account.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: transaction deposit account
type: Ontology Class
---

# transaction deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount>

## Definition

deposit account from which the depositor / account holder is permitted to make transfers or withdrawals by negotiable / transferable instruments, payment orders of withdrawal, telephone transfers, and so forth, and that may be accessible via an electronic device such as an automated teller machine (ATM), remote service unit (RSU), mobile device, and by debit card

## Relationships

- **Subclass of**: [DepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md)

## Annotations

- **label**: transaction deposit account
- **definition**: deposit account from which the depositor / account holder is permitted to make transfers or withdrawals by negotiable / transferable instruments, payment orders of withdrawal, telephone transfers, and so forth, and that may be accessible via an electronic device such as an automated teller machine (ATM), remote service unit (RSU), mobile device, and by debit card
- **explanatoryNote**: Excluded from transaction accounts are savings deposits (both money market deposit accounts (MMDAs) and other savings deposits), even though such deposits permit some third-party transfers. However, an account that otherwise meets the definition of a savings deposit but that authorizes or permits the depositor to exceed the transfer limitations specified for that account shall be reported as a transaction account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
