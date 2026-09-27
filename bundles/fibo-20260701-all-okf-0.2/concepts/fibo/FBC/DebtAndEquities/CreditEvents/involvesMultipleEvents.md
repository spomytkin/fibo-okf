---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: involves multiple events
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that the restructuring spans more than one credit event
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationRestructuring.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationRestructuring
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/involvesMultipleEvents
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: involves multiple events
type: Ontology Property
---

# involves multiple events

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/involvesMultipleEvents>

## Definition

indicates that the restructuring spans more than one credit event

## Relationships

- **Domain**: [ObligationRestructuring](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationRestructuring.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): involves multiple events
- **definition** (en): indicates that the restructuring spans more than one credit event

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
