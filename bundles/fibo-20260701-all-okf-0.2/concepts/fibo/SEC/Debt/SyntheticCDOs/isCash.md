---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is cash
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Whether the CDO has an underlying pool of real assets. This is No: the CDO has a synthetic pool of underlying
      assets.'
  domain:
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/isCash
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: is cash
type: Ontology Property
---

# is cash

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/isCash>

## Definition

Whether the CDO has an underlying pool of real assets. This is No: the CDO has a synthetic pool of underlying assets.

## Relationships

- **Domain**: [SyntheticCDOTranche](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is cash
- **definition** (en): Whether the CDO has an underlying pool of real assets. This is No: the CDO has a synthetic pool of underlying assets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
