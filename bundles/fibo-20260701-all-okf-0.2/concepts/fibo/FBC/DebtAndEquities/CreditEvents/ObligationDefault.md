---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: obligation default
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event triggered as a result of an obligation-specific default
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/DefaultEvent
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationDefault
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: obligation default
type: Ontology Class
---

# obligation default

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationDefault>

## Definition

credit event triggered as a result of an obligation-specific default

## Relationships

- **Subclass of**: [DefaultEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/DefaultEvent.md)
- **Subclass of**: [ObligationSpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md)

## Annotations

- **label** (en): obligation default
- **definition** (en): credit event triggered as a result of an obligation-specific default

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
