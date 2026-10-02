---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: individual transaction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event that has a monetary impact and is documented in the records associated with an account
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasPostingDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionDate
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionDescription
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Merchant
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/involvesMerchant
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionCategory
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionSubcategory
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionIdentifier
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: individual transaction
type: Ontology Class
---

# individual transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction>

## Definition

event that has a monetary impact and is documented in the records associated with an account

## Relationships

- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[appliesToAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount.md)**: exact qualified cardinality 1 of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- **[hasPostingDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasPostingDate.md)**: exact qualified cardinality 1 of type [PostingDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate.md)
- **[hasTransactionDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionDate.md)**: exact qualified cardinality 1 of type [TransactionDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md)
- **[hasTransactionDescription](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionDescription.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[involvesMerchant](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/involvesMerchant.md)**: min qualified cardinality 0 of type [Merchant](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/Merchant.md)
- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: min qualified cardinality 0 of type [TransactionEvent](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [TransactionCategory](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionCategory.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: min qualified cardinality 0 of type [TransactionSubcategory](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionSubcategory.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: max qualified cardinality 1 of type [TransactionIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionIdentifier.md)
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: all values from of type [TransactionRecord](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)

## Annotations

- **label**: individual transaction
- **definition**: event that has a monetary impact and is documented in the records associated with an account

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
