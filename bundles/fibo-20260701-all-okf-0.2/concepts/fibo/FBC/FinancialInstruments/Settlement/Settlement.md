---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: settlement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: act of finalizing a transaction, including but not limited to finalizing accounting, exchanging consideration,
      and/or legally recording documents, as applicable
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/Settlement
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: settlement
type: Ontology Class
---

# settlement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/Settlement>

## Definition

act of finalizing a transaction, including but not limited to finalizing accounting, exchanging consideration, and/or legally recording documents, as applicable

## Relationships

- **Subclass of**: [ContractLifecycleEvent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md)

## Annotations

- **label** (en): settlement
- **definition**: act of finalizing a transaction, including but not limited to finalizing accounting, exchanging consideration, and/or legally recording documents, as applicable

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
