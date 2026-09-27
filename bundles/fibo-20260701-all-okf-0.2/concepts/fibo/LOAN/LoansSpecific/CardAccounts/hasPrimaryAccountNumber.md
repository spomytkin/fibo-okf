---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has primary account number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the account number displayed on the face of the card
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: modeled independently of 'identifies' in order to circumvent circular reasoning challenges
  domain:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
  range:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasPrimaryAccountNumber
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: has primary account number
type: Ontology Property
---

# has primary account number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasPrimaryAccountNumber>

## Definition

specifies the account number displayed on the face of the card

## Relationships

- **Domain**: [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- **Range**: [PrimaryCardAccountNumber](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md)

## Annotations

- **label**: has primary account number
- **definition**: specifies the account number displayed on the face of the card
- **editorialNote**: modeled independently of 'identifies' in order to circumvent circular reasoning challenges

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
