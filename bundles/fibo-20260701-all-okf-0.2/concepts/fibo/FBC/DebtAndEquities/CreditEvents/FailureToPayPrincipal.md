---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: failure to pay principal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: default event that where either an expected principal payment is missed altogether or the amount paid is less than
      the required amount
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/FailureToPay.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FailureToPay
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FailureToPayPrincipal
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: failure to pay principal
type: Ontology Class
---

# failure to pay principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/FailureToPayPrincipal>

## Definition

default event that where either an expected principal payment is missed altogether or the amount paid is less than the required amount

## Relationships

- **Subclass of**: [FailureToPay](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/FailureToPay.md)

## Annotations

- **label** (en): failure to pay principal
- **definition** (en): default event that where either an expected principal payment is missed altogether or the amount paid is less than the required amount

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
