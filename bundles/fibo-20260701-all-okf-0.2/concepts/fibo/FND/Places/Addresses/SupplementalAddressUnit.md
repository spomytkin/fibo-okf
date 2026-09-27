---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: supplemental address unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: address component that includes a specific route, box, apartment, condominium or other indicator or unit associated
      with a specific address
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
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressUnit
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: supplemental address unit
type: Ontology Class
---

# supplemental address unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressUnit>

## Definition

address component that includes a specific route, box, apartment, condominium or other indicator or unit associated with a specific address

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: supplemental address unit
- **definition**: address component that includes a specific route, box, apartment, condominium or other indicator or unit associated with a specific address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
