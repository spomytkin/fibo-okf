---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has settlement method
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the strategy for settlement from a delivery perspective
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/Settlement/DeliveryMethod.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/DeliveryMethod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/hasDeliveryMethod
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: has settlement method
type: Ontology Property
---

# has settlement method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/hasDeliveryMethod>

## Definition

specifies the strategy for settlement from a delivery perspective

## Relationships

- **Domain**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- **Range**: [DeliveryMethod](/concepts/fibo/FBC/FinancialInstruments/Settlement/DeliveryMethod.md)
- **Subproperty of**: [hasStrategy](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasStrategy.md)

## Annotations

- **label** (en): has settlement method
- **definition**: specifies the strategy for settlement from a delivery perspective

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
