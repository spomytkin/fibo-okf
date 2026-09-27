---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: investment account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account that provides a record of deposits of funds and/or securities held at a financial institution
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The typical objectives of an investment account are to achieve long term growth, income or capital preservation
      from the deposited asset portfolio. Investment accounts are typically not insured.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: investment account
type: Ontology Class
---

# investment account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentAccount>

## Definition

account that provides a record of deposits of funds and/or securities held at a financial institution

## Relationships

- **Subclass of**: [InvestmentOrDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/InvestmentOrDepositAccount.md)

## Constraints

- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: investment account
- **definition**: account that provides a record of deposits of funds and/or securities held at a financial institution
- **explanatoryNote**: The typical objectives of an investment account are to achieve long term growth, income or capital preservation from the deposited asset portfolio. Investment accounts are typically not insured.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
