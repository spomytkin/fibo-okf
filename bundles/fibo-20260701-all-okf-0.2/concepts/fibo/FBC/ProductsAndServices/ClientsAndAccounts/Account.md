---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: container for records associated with a business arrangement for regular transactions and services
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In general, an account is associated with a contractual relationship between a buyer and seller under which payment
      may be made at a later time. General ledger accounts are an exception to this, however, and typically do not have account
      holders, including internal account holders. They may, on the other hand, have responsible parties.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasCloseDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasOpenDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasRecord
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isHeldBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: account
type: Ontology Class
---

# account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account>

## Definition

container for records associated with a business arrangement for regular transactions and services

## Constraints

- **[hasBalance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasBalance.md)**: some values from of type [Balance](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- **[hasCloseDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasCloseDate.md)**: min qualified cardinality 0 of type [CloseDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate.md)
- **[hasOpenDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasOpenDate.md)**: exact qualified cardinality 1 of type [OpenDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate.md)
- **[hasRecord](/concepts/fibo/FND/Arrangements/Documents/hasRecord.md)**: min qualified cardinality 0 of type [TransactionRecord](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)
- **[isHeldBy](/concepts/fibo/FND/Relations/Relations/isHeldBy.md)**: min qualified cardinality 0 of type [AccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [AccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [AccountProvider](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)

## Annotations

- **label**: account
- **definition**: container for records associated with a business arrangement for regular transactions and services
- **explanatoryNote**: In general, an account is associated with a contractual relationship between a buyer and seller under which payment may be made at a later time. General ledger accounts are an exception to this, however, and typically do not have account holders, including internal account holders. They may, on the other hand, have responsible parties.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
