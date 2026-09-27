---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has credit card network
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the underlying network for credit card product
  range:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCreditCardNetwork
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: has credit card network
type: Ontology Property
---

# has credit card network

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCreditCardNetwork>

## Definition

indicates the underlying network for credit card product

## Relationships

- **Range**: [CreditCardNetwork](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork.md)
- **Subproperty of**: [isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)

## Annotations

- **label**: has credit card network
- **definition**: indicates the underlying network for credit card product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
