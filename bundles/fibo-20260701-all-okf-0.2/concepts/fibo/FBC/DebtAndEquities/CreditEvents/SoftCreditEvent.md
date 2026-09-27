---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: soft credit event
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: default event that is repairable
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the default is not repaired within a grace period, then a failure to repair (failure to pay) credit event is
      triggered, potentially as a hard default.
  disjoint_with:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/HardCreditEvent.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/HardCreditEvent
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/SoftCreditEvent
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: soft credit event
type: Ontology Class
---

# soft credit event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/SoftCreditEvent>

## Definition

default event that is repairable

## Relationships

- **Subclass of**: [DefaultEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md)

## Constraints

- **Disjoint with**: [HardCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/HardCreditEvent.md)

## Annotations

- **label** (en): soft credit event
- **definition** (en): default event that is repairable
- **explanatoryNote** (en): If the default is not repaired within a grace period, then a failure to repair (failure to pay) credit event is triggered, potentially as a hard default.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
