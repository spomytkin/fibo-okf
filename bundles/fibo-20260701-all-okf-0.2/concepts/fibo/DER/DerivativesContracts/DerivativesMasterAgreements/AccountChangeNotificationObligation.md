---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: account change notification obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: obligation to notify a counterparty of any changes in account details
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Example text: "Either party may change its account for receiving a payment or delivery by giving notice to the
      other party at least five Local Business Days prior to the scheduled date for the payment or delivery to which such
      change applies unless such other party gives timely notice of a reasonable objection to such change." Note that the
      notice period is given as a fact about the general kind of obligation which is Master Agreement Change notification
      Obligation.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/NotificationObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/NotificationObligation
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/AccountChangeNotificationObligation
sources:
- id: fibo-source-d9f057f57c
  resource: references/fibo/DER/DerivativesContracts/DerivativesMasterAgreements.rdf
  sha256: d9f057f57c2fbab0f06a73b8281b7d476e79c36502bb7a47cc8b00f51ec459d2
  title: FIBO source DER/DerivativesContracts/DerivativesMasterAgreements.rdf
title: account change notification obligation
type: Ontology Class
---

# account change notification obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/AccountChangeNotificationObligation>

## Definition

obligation to notify a counterparty of any changes in account details

## Relationships

- **Subclass of**: [NotificationObligation](/concepts/fibo/FND/Law/LegalCapacity/NotificationObligation.md)

## Annotations

- **label** (en): account change notification obligation
- **definition** (en): obligation to notify a counterparty of any changes in account details
- **example** (en): Example text: "Either party may change its account for receiving a payment or delivery by giving notice to the other party at least five Local Business Days prior to the scheduled date for the payment or delivery to which such change applies unless such other party gives timely notice of a reasonable objection to such change." Note that the notice period is given as a fact about the general kind of obligation which is Master Agreement Change notification Obligation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
