---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is strippable
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether or not the instrument can be stripped, so that interest and principal may be traded separately
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isStrippable
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: is strippable
type: Ontology Property
---

# is strippable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isStrippable>

## Definition

indicates whether or not the instrument can be stripped, so that interest and principal may be traded separately

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is strippable
- **definition**: indicates whether or not the instrument can be stripped, so that interest and principal may be traded separately

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
