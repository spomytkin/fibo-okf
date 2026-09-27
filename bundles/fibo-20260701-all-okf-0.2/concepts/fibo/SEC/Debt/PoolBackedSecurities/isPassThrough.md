---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is pass through
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the cash flows from the underlying asset pool are passed through to the investor by way of redemption
      payments
  domain:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/isPassThrough
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: is pass through
type: Ontology Property
---

# is pass through

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/isPassThrough>

## Definition

indicates whether the cash flows from the underlying asset pool are passed through to the investor by way of redemption payments

## Relationships

- **Domain**: [PoolBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is pass through
- **definition** (en): indicates whether the cash flows from the underlying asset pool are passed through to the investor by way of redemption payments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
