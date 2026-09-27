---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is legal opinion available
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether a legal opinion exists for a given municipal bond
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isLegalOpinionAvailable
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: is legal opinion available
type: Ontology Property
---

# is legal opinion available

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isLegalOpinionAvailable>

## Definition

indicates whether a legal opinion exists for a given municipal bond

## Relationships

- **Domain**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is legal opinion available
- **definition**: indicates whether a legal opinion exists for a given municipal bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
