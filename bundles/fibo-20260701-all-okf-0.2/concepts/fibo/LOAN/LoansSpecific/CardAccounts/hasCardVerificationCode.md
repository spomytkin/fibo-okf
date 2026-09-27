---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has card verification code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'links a credit card to either: (1) magnetic-stripe data, or (2) printed security features that are used to protect
      data integrity and limit alteration, counterfeiting and fraud generally'
  domain:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
  range:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCardVerificationCode
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: has card verification code
type: Ontology Property
---

# has card verification code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/hasCardVerificationCode>

## Definition

links a credit card to either: (1) magnetic-stripe data, or (2) printed security features that are used to protect data integrity and limit alteration, counterfeiting and fraud generally

## Relationships

- **Domain**: [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- **Range**: [CardVerificationCodeValue](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md)

## Annotations

- **label**: has card verification code
- **definition**: links a credit card to either: (1) magnetic-stripe data, or (2) printed security features that are used to protect data integrity and limit alteration, counterfeiting and fraud generally

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
