---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account statement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: periodic summary of account activity for a given period of time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Common kinds of account statements include checking account statements, usually provided monthly, and brokerage
      account statements, which are provided monthly or quarterly, depending on the terms of the account agreement. Monthly
      credit card bills are also considered account statements.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasEndingBalance
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasStartingBalance
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/recordsTransaction
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasReportingPeriod
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Record
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountStatement
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account statement
type: Ontology Class
---

# account statement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountStatement>

## Definition

periodic summary of account activity for a given period of time

## Relationships

- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)
- **Subclass of**: [Record](<https://www.omg.org/spec/Commons/Documents/Record>)

## Constraints

- **[appliesToAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount.md)**: exact qualified cardinality 1 of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- **[hasEndingBalance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasEndingBalance.md)**: max qualified cardinality 1 of type [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **[hasStartingBalance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasStartingBalance.md)**: max qualified cardinality 1 of type [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **[recordsTransaction](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/recordsTransaction.md)**: some values from of type [IndividualTransaction](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md)
- **[hasReportingPeriod](/concepts/fibo/FND/Arrangements/Documents/hasReportingPeriod.md)**: max qualified cardinality 1 of type [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)

## Annotations

- **label**: account statement
- **definition**: periodic summary of account activity for a given period of time
- **explanatoryNote**: Common kinds of account statements include checking account statements, usually provided monthly, and brokerage account statements, which are provided monthly or quarterly, depending on the terms of the account agreement. Monthly credit card bills are also considered account statements.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
