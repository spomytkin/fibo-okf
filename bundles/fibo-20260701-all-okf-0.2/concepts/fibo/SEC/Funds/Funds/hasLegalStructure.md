---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has legal structure
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the legal form that the fund takes
  domain:
  - concept: /concepts/fibo/SEC/Securities/Pools/PooledFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
  range:
  - concept: /concepts/fibo/SEC/Funds/Funds/LegalFundStructure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/LegalFundStructure
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/hasLegalStructure
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: has legal structure
type: Ontology Property
---

# has legal structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/hasLegalStructure>

## Definition

indicates the legal form that the fund takes

## Relationships

- **Domain**: [PooledFund](/concepts/fibo/SEC/Securities/Pools/PooledFund.md)
- **Range**: [LegalFundStructure](/concepts/fibo/SEC/Funds/Funds/LegalFundStructure.md)

## Annotations

- **label** (en): has legal structure
- **definition** (en): indicates the legal form that the fund takes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
