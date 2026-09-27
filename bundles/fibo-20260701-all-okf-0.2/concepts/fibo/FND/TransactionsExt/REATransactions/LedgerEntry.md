---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ledger entry
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasPostingDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/LedgerEntry
sources:
- id: fibo-source-a4a03421b9
  resource: references/fibo/FND/TransactionsExt/REATransactions.rdf
  sha256: a4a03421b94997c356ef5975cbdab23f45cffa4cec464b870e344d6c77d8678a
  title: FIBO source FND/TransactionsExt/REATransactions.rdf
title: ledger entry
type: Ontology Class
---

# ledger entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/LedgerEntry>

## Relationships

- **Subclass of**: [DatedCollectionConstituent](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[hasPostingDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasPostingDate.md)**: exact qualified cardinality 1 of type [PostingDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate.md)
- **[hasTransactionDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasTransactionDate.md)**: exact qualified cardinality 1 of type [TransactionDate](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md)
- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: some values from of type [LedgerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)

## Annotations

- **label** (en): ledger entry

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
