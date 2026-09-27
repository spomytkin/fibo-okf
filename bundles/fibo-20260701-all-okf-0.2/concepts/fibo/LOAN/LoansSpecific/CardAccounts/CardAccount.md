---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: card account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: account whose terms and conditions are defined in a card agreement that is represented by a payment card
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/Cardholder
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/hasPrimaryAccountHolder
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/isLinkedToAccount
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardProduct
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isSignifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: card account
type: Ontology Class
---

# card account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount>

## Definition

account whose terms and conditions are defined in a card agreement that is represented by a payment card

## Relationships

- **Subclass of**: [CustomerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)

## Constraints

- **[hasPrimaryAccountHolder](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/hasPrimaryAccountHolder.md)**: some values from of type [Cardholder](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/Cardholder.md)
- **[isLinkedToAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/isLinkedToAccount.md)**: min qualified cardinality 0 of type [CustomerAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: some values from of type [CardProduct](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardProduct.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [PaymentCardAgreement](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md)
- **[isSignifiedBy](<https://www.omg.org/spec/Commons/Designators/isSignifiedBy>)**: some values from of type [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [PrimaryCardAccountNumber](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md)

## Annotations

- **label**: card account
- **definition**: account whose terms and conditions are defined in a card agreement that is represented by a payment card

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
