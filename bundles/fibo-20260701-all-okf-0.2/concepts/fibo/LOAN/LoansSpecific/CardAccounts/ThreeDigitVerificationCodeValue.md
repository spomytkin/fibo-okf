---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: three-digit verification code or value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: card verification code that is the rightmost three-digit value printed in the signature panel area on the back
      of the card
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.pcisecuritystandards.org/pci_security/glossary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/ThreeDigitVerificationCodeValue
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: three-digit verification code or value
type: Ontology Class
---

# three-digit verification code or value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/ThreeDigitVerificationCodeValue>

## Definition

card verification code that is the rightmost three-digit value printed in the signature panel area on the back of the card

## Relationships

- **Subclass of**: [CardVerificationCodeValue](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md)

## Annotations

- **label**: three-digit verification code or value
- **definition**: card verification code that is the rightmost three-digit value printed in the signature panel area on the back of the card
- **adaptedFrom**: https://www.pcisecuritystandards.org/pci_security/glossary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
