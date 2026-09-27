---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: addressing scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating addresses to objects
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/IdentifiersAndIndices/IndexingScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/IndexingScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressingScheme
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: addressing scheme
type: Ontology Class
---

# addressing scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressingScheme>

## Definition

system for allocating addresses to objects

## Relationships

- **Subclass of**: [IndexingScheme](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/IndexingScheme.md)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: all values from of type [Address](/concepts/fibo/FND/Places/Addresses/Address.md)

## Annotations

- **label**: addressing scheme
- **definition**: system for allocating addresses to objects

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
