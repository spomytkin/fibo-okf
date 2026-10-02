---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has structure name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies an identifier for a building, house, office complex, shopping center, or other structure or group of
      structures
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/StructureName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StructureName
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStructureName
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has structure name
type: Ontology Property
---

# has structure name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasStructureName>

## Definition

specifies an identifier for a building, house, office complex, shopping center, or other structure or group of structures

## Relationships

- **Domain**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **Range**: [StructureName](/concepts/fibo/FND/Places/Addresses/StructureName.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has structure name
- **definition**: specifies an identifier for a building, house, office complex, shopping center, or other structure or group of structures

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
