---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: record of transactions associated with an account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: The date a particular transaction record is closed typically corresponds to (and may precede) the date the account
      is closed, though in the case of certain accounts, such as a credit card account, if a customer is issued a new account
      or card number due to loss, fraud, or for some other reason, it is possible that multiple transaction records would
      be associated with the account. In that case, the close date might correspond to the date that a hold was placed on
      the original account.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasCloseDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasOpenDate
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionRecordStatus
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Record
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: transaction record
type: Ontology Class
---

# transaction record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord>

## Definition

record of transactions associated with an account

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- **Subclass of**: [Record](<https://www.omg.org/spec/Commons/Documents/Record>)
- **Subclass of**: [Registry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry>)

## Constraints

- **[appliesToAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/appliesToAccount.md)**: exact qualified cardinality 1 of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- **[hasCloseDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasCloseDate.md)**: min qualified cardinality 0 of type [CloseDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate.md)
- **[hasOpenDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasOpenDate.md)**: min qualified cardinality 0 of type [OpenDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate.md)
- **[hasTransactionRecordStatus](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionRecordStatus.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [IndividualTransaction](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: max qualified cardinality 1 of type [TransactionRecordIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: exact qualified cardinality 1 of type [AccountProvider](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)

## Annotations

- **label**: transaction record
- **definition**: record of transactions associated with an account
- **usageNote**: The date a particular transaction record is closed typically corresponds to (and may precede) the date the account is closed, though in the case of certain accounts, such as a credit card account, if a customer is issued a new account or card number due to loss, fraud, or for some other reason, it is possible that multiple transaction records would be associated with the account. In that case, the close date might correspond to the date that a hold was placed on the original account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
