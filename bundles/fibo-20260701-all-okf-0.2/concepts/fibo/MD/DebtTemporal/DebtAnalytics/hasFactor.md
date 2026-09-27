---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has factor
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
  range:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/PoolFactor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasFactor
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: has factor
type: Ontology Property
---

# has factor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/hasFactor>

## Relationships

- **Domain**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)
- **Range**: [PoolFactor](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/PoolFactor.md)

## Annotations

- **label** (en): has factor

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
