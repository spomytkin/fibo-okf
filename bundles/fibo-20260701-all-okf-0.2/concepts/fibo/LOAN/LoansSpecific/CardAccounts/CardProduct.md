---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: card product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial product involving the issuance of credit, debit, or other payment cards
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCreditCardNetwork
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/usesCurrency
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasCountry
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Locations/CountrySubdivision
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasSubdivision
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardProduct
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: card product
type: Ontology Class
---

# card product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardProduct>

## Definition

financial product involving the issuance of credit, debit, or other payment cards

## Relationships

- **Subclass of**: [FinancialProduct](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)

## Constraints

- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: some values from of type [CardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
- **[hasCreditCardNetwork](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/hasCreditCardNetwork.md)**: min qualified cardinality 0 of type [CreditCardNetwork](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork.md)
- **[usesCurrency](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/usesCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasCountry](<https://www.omg.org/spec/Commons/Locations/hasCountry>)**: exact qualified cardinality 1 of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[hasSubdivision](<https://www.omg.org/spec/Commons/Locations/hasSubdivision>)**: min qualified cardinality 0 of type [CountrySubdivision](<https://www.omg.org/spec/Commons/Locations/CountrySubdivision>)

## Annotations

- **label**: card product
- **definition**: financial product involving the issuance of credit, debit, or other payment cards

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
