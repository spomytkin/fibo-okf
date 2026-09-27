---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has original place of listing
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the original exchange that listed the security
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasOriginalPlaceOfListing
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: has original place of listing
type: Ontology Property
---

# has original place of listing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasOriginalPlaceOfListing>

## Definition

indicates the original exchange that listed the security

## Relationships

- **Range**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Annotations

- **label**: has original place of listing
- **definition**: indicates the original exchange that listed the security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
