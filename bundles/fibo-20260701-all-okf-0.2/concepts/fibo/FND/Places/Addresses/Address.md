---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: index to a location to which communications may be delivered
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Locations/Location
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/isIndexTo
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressingScheme
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/IdentifiersAndIndices/Index.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/Index
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: address
type: Ontology Class
---

# address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Address>

## Definition

index to a location to which communications may be delivered

## Relationships

- **Subclass of**: [Index](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/Index.md)

## Constraints

- **[isIndexTo](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/isIndexTo.md)**: exact qualified cardinality 1 of type [Location](<https://www.omg.org/spec/Commons/Locations/Location>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: min qualified cardinality 0 of type [AddressingScheme](/concepts/fibo/FND/Places/Addresses/AddressingScheme.md)

## Annotations

- **label** (en): address
- **definition**: index to a location to which communications may be delivered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
