---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: card authentication value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: card verification value specifically for JCB payment cards
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CAV
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.pcisecuritystandards.org/pci_security/glossary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/MagneticStripeVerificationCodeValue.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/MagneticStripeVerificationCodeValue
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAuthenticationValue
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: card authentication value
type: Ontology Class
---

# card authentication value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAuthenticationValue>

## Definition

card verification value specifically for JCB payment cards

## Relationships

- **Subclass of**: [MagneticStripeVerificationCodeValue](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/MagneticStripeVerificationCodeValue.md)

## Annotations

- **label**: card authentication value
- **definition**: card verification value specifically for JCB payment cards
- **abbreviation**: CAV
- **adaptedFrom**: https://www.pcisecuritystandards.org/pci_security/glossary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
