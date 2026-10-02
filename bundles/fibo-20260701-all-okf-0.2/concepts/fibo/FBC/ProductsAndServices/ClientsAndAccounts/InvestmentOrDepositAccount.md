---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment or deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account associated with a product or service that requires the account holder to provide funds for management by
      the account provider
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The account holder may or may not be entitled to consideration in exchange for providing such funds, for example,
      interest, depending on the type of account and the terms and conditions associated with it. Also, there may be fees
      associated with management services provided by the account provider. Note too that this may be an internal account
      held on behalf of an institution or a customer account.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: investment or deposit account
type: Ontology Class
---

# investment or deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount>

## Definition

account associated with a product or service that requires the account holder to provide funds for management by the account provider

## Relationships

- **Subclass of**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: investment or deposit account
- **definition**: account associated with a product or service that requires the account holder to provide funds for management by the account provider
- **explanatoryNote**: The account holder may or may not be entitled to consideration in exchange for providing such funds, for example, interest, depending on the type of account and the terms and conditions associated with it. Also, there may be fees associated with management services provided by the account provider. Note too that this may be an internal account held on behalf of an institution or a customer account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
