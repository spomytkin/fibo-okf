---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is sub-fund of
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a pooled fund to a parent fund
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/PooledFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
  inverse_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/hasSubFund.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/hasSubFund
  range:
  - concept: /concepts/fibo/SEC/Securities/Pools/PooledFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/isPartOf
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isSubFundOf
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: is sub-fund of
type: Ontology Property
---

# is sub-fund of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/isSubFundOf>

## Definition

relates a pooled fund to a parent fund

## Relationships

- **Domain**: [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)
- **Inverse of**: [hasSubFund](/concepts/fibo/SEC/Funds/Funds/hasSubFund.md)
- **Range**: [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)
- **Subproperty of**: [isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)

## Annotations

- **label** (en): is sub-fund of
- **definition** (en): relates a pooled fund to a parent fund

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
