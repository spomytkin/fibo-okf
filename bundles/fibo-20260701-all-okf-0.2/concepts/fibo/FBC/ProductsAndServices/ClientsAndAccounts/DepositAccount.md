---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: deposit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account that provides a record of money placed with a depository institution for safekeeping and management
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Deposit accounts include savings accounts, money market accounts, and transactional accounts, such as demand deposit
      accounts, among others.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The account holder has the right to withdraw deposited funds, as set forth in the terms and conditions governing
      the account agreement. Deposit accounts may be insured up to a certain amount, depending on the jurisdiction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: deposit account
type: Ontology Class
---

# deposit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount>

## Definition

account that provides a record of money placed with a depository institution for safekeeping and management

## Relationships

- **Subclass of**: [BankingProduct](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BankingProduct.md)
- **Subclass of**: [InvestmentOrDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [DepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)

## Annotations

- **label**: deposit account
- **definition**: account that provides a record of money placed with a depository institution for safekeeping and management
- **example**: Deposit accounts include savings accounts, money market accounts, and transactional accounts, such as demand deposit accounts, among others.
- **explanatoryNote**: The account holder has the right to withdraw deposited funds, as set forth in the terms and conditions governing the account agreement. Deposit accounts may be insured up to a certain amount, depending on the jurisdiction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
