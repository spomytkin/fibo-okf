---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is subordinated
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the security is a subordinated security, meaning that the security has a lower priority than
      another security so that when the assets are liquidated this one is not first in line
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isSubordinated
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: is subordinated
type: Ontology Property
---

# is subordinated

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isSubordinated>

## Definition

indicates whether the security is a subordinated security, meaning that the security has a lower priority than another security so that when the assets are liquidated this one is not first in line

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is subordinated
- **definition**: indicates whether the security is a subordinated security, meaning that the security has a lower priority than another security so that when the assets are liquidated this one is not first in line

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
