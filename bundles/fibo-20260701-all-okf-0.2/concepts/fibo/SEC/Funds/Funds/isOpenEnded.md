---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is open ended
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the fund is an open-end/closed-end fund
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/PooledFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isOpenEnded
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: is open ended
type: Ontology Property
---

# is open ended

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isOpenEnded>

## Definition

indicates whether the fund is an open-end/closed-end fund

## Relationships

- **Domain**: [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is open ended
- **definition** (en): indicates whether the fund is an open-end/closed-end fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
