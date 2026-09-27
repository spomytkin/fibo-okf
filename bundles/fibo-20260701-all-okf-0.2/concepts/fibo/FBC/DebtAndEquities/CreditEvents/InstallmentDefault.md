---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: installment default
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: default event involving non-payment of several installment payments as scheduled in the terms of the agreement,
      or non-payment of a call by the beneficial owner
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The latter may result in a court action by the issuer or the sale of the securities to recover costs and/or a forfeit
      of partially paid securities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InstallmentDefault
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: installment default
type: Ontology Class
---

# installment default

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InstallmentDefault>

## Definition

default event involving non-payment of several installment payments as scheduled in the terms of the agreement, or non-payment of a call by the beneficial owner

## Relationships

- **Subclass of**: [DefaultEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md)

## Annotations

- **label** (en): installment default
- **definition** (en): default event involving non-payment of several installment payments as scheduled in the terms of the agreement, or non-payment of a call by the beneficial owner
- **explanatoryNote** (en): The latter may result in a court action by the issuer or the sale of the securities to recover costs and/or a forfeit of partially paid securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
