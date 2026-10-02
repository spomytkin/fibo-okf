---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: smart card
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: payment card that has integrated circuits embedded within it
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.pcisecuritystandards.org/pci_security/glossary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The circuits, also referred to as the 'chip,' contain payment card data including but not limited to data equivalent
      to the magnetic-stripe data.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/SmartCard
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: smart card
type: Ontology Class
---

# smart card

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/SmartCard>

## Definition

payment card that has integrated circuits embedded within it

## Relationships

- **Subclass of**: [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)

## Annotations

- **label**: smart card
- **definition**: payment card that has integrated circuits embedded within it
- **adaptedFrom**: https://www.pcisecuritystandards.org/pci_security/glossary
- **explanatoryNote**: The circuits, also referred to as the 'chip,' contain payment card data including but not limited to data equivalent to the magnetic-stripe data.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
