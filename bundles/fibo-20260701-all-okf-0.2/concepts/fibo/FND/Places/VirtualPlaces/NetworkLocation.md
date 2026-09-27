---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: network location
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a virtual location that may be identified by a network address (an identifier for a node or interface)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Locations/VirtualLocation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/NetworkLocation
sources:
- id: fibo-source-408986d983
  resource: references/fibo/FND/Places/VirtualPlaces.rdf
  sha256: 408986d983df3f87901b90ff49e3ba3f323f94111338f7674037f481104e6007
  title: FIBO source FND/Places/VirtualPlaces.rdf
title: network location
type: Ontology Class
---

# network location

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/NetworkLocation>

## Definition

a virtual location that may be identified by a network address (an identifier for a node or interface)

## Relationships

- **Subclass of**: [VirtualLocation](<https://www.omg.org/spec/Commons/Locations/VirtualLocation>)

## Constraints

- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: exact qualified cardinality 1 of type [Address](/concepts/fibo/FND/Places/Addresses/Address.md)

## Annotations

- **label**: network location
- **definition**: a virtual location that may be identified by a network address (an identifier for a node or interface)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
