---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: virtual address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: address identifying a virtual, i.e. non-physical, location
  disjoint_with:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddress.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/Address.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/VirtualAddress
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: virtual address
type: Ontology Class
---

# virtual address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/VirtualAddress>

## Definition

address identifying a virtual, i.e. non-physical, location

## Relationships

- **Subclass of**: [Address](/concepts/fibo/FND/Places/Addresses/Address.md)

## Constraints

- **Disjoint with**: [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: virtual address
- **definition**: address identifying a virtual, i.e. non-physical, location

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
