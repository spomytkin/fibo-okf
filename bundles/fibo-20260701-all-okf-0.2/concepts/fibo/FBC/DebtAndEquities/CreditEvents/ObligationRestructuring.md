---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: obligation restructuring
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event that materially impacts an obligation, such as an interest rate reduction, principal reduction, deferral
      of interest or principal, change in priority ranking, or change in currency or composition of payment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationRestructuring
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: obligation restructuring
type: Ontology Class
---

# obligation restructuring

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationRestructuring>

## Definition

credit event that materially impacts an obligation, such as an interest rate reduction, principal reduction, deferral of interest or principal, change in priority ranking, or change in currency or composition of payment

## Relationships

- **Subclass of**: [ObligationSpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent.md)

## Annotations

- **label** (en): obligation restructuring
- **definition** (en): credit event that materially impacts an obligation, such as an interest rate reduction, principal reduction, deferral of interest or principal, change in priority ranking, or change in currency or composition of payment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
