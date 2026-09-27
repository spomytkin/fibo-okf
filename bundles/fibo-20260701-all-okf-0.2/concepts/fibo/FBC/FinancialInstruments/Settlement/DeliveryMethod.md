---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: delivery method
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: method and commitment to transfer a commodity, currency, security, cash or another instrument as defined in the
      settlement terms of the contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  - https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualCommitment
  subclass_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/DistributionStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/DistributionStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/DeliveryMethod
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: delivery method
type: Ontology Class
---

# delivery method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/DeliveryMethod>

## Definition

method and commitment to transfer a commodity, currency, security, cash or another instrument as defined in the settlement terms of the contract

## Relationships

- **Subclass of**: [DistributionStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/DistributionStrategy.md)

## Annotations

- **label** (en): delivery method
- **definition**: method and commitment to transfer a commodity, currency, security, cash or another instrument as defined in the settlement terms of the contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
