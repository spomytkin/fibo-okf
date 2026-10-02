---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan or credit account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account associated with a service in which the account holder receives funds from the account provider under certain
      terms and conditions for repayment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that this may be an internal account held on behalf of an institution or a customer account, such as a line
      of credit account associated with an internal line of business.
  disjoint_with:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: loan or credit account
type: Ontology Class
---

# loan or credit account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount>

## Definition

account associated with a service in which the account holder receives funds from the account provider under certain terms and conditions for repayment

## Relationships

- **Subclass of**: [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Constraints

- **Disjoint with**: [InvestmentOrDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md)

## Annotations

- **label**: loan or credit account
- **definition**: account associated with a service in which the account holder receives funds from the account provider under certain terms and conditions for repayment
- **explanatoryNote**: Note that this may be an internal account held on behalf of an institution or a customer account, such as a line of credit account associated with an internal line of business.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
