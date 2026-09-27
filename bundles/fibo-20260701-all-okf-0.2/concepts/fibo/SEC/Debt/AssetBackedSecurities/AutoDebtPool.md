---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: auto debt pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt pool of loans and/or leases that are motor vehicle-related
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasPart
    value: N19f5538e259241209f0fd757b6b834c3
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/AutoDebtPool
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: auto debt pool
type: Ontology Class
---

# auto debt pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/AutoDebtPool>

## Definition

debt pool of loans and/or leases that are motor vehicle-related

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)**: some values from value `N19f5538e259241209f0fd757b6b834c3`

## Annotations

- **label** (en): auto debt pool
- **definition** (en): debt pool of loans and/or leases that are motor vehicle-related

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
