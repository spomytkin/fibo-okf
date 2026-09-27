---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: structure name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: name for a building, house, office complex, shopping center, or other structure or group of structures
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include 'McCoy Center', which is the name of the office complex where JPMorgan Chase's Polaris facility
      is located, 'Apple Park', which is the name of the corporate headquarters of Apple, Inc., and 'Howells Bridge Cottage',
      which is the name of a very old cottage in Cornwall.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/AddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressComponent
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Designators/Name
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StructureName
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: structure name
type: Ontology Class
---

# structure name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StructureName>

## Definition

name for a building, house, office complex, shopping center, or other structure or group of structures

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)
- **Subclass of**: [Name](<https://www.omg.org/spec/Commons/Designators/Name>)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: structure name
- **definition**: name for a building, house, office complex, shopping center, or other structure or group of structures
- **example**: Examples include 'McCoy Center', which is the name of the office complex where JPMorgan Chase's Polaris facility is located, 'Apple Park', which is the name of the corporate headquarters of Apple, Inc., and 'Howells Bridge Cottage', which is the name of a very old cottage in Cornwall.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
