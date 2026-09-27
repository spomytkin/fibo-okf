---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit card network
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for the network that authorizes, processes, and sets the terms of credit card transactions, as well
      as transfers payments between shoppers, merchants, and their banks
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Mastercard, Visa, American Express, Discover
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardProduct
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: credit card network
type: Ontology Class
---

# credit card network

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork>

## Definition

classifier for the network that authorizes, processes, and sets the terms of credit card transactions, as well as transfers payments between shoppers, merchants, and their banks

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [CardProduct](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardProduct.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: credit card network
- **definition**: classifier for the network that authorizes, processes, and sets the terms of credit card transactions, as well as transfers payments between shoppers, merchants, and their banks
- **example**: Mastercard, Visa, American Express, Discover

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
