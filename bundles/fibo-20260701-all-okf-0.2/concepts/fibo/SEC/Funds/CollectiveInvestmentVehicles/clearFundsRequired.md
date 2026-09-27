---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: clear funds required
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether cleared funds may be required before a subscription order can be executed.
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/clearFundsRequired
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: clear funds required
type: Ontology Property
---

# clear funds required

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/clearFundsRequired>

## Definition

Whether cleared funds may be required before a subscription order can be executed.

## Relationships

- **Domain**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): clear funds required
- **definition** (en): Whether cleared funds may be required before a subscription order can be executed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
