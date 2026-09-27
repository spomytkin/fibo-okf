---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: post code area
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: physical area uniquely identified by some postal code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/GeographicRegion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostCodeArea
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: post code area
type: Ontology Class
---

# post code area

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PostCodeArea>

## Definition

physical area uniquely identified by some postal code

## Relationships

- **Subclass of**: [GeographicRegion](<https://www.omg.org/spec/Commons/Locations/GeographicRegion>)

## Annotations

- **label** (en): post code area
- **definition**: physical area uniquely identified by some postal code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
