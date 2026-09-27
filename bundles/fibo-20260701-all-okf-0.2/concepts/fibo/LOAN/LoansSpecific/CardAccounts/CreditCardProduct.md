---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card product
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: card product allowing the holder to purchase goods or services on credit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCreditCardNetwork
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCard
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardProduct
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardProduct
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: credit card product
type: Ontology Class
---

# credit card product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardProduct>

## Definition

card product allowing the holder to purchase goods or services on credit

## Relationships

- **Subclass of**: [CardProduct](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardProduct.md)

## Constraints

- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: some values from of type [CreditCardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md)
- **[hasCreditCardNetwork](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/hasCreditCardNetwork.md)**: exact qualified cardinality 1 of type [CreditCardNetwork](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork.md)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [CreditCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCard.md)

## Annotations

- **label**: credit card product
- **definition**: card product allowing the holder to purchase goods or services on credit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
