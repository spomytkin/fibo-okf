---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: secondary unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: address component that identifies an individual unit within a larger structure, such as an apartment, office, hangar,
      slip, mailbox, and so forth, at a given street address
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitDesignator
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitIndicator
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/AddressComponent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/AddressComponent
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnit
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: secondary unit
type: Ontology Class
---

# secondary unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnit>

## Definition

address component that identifies an individual unit within a larger structure, such as an apartment, office, hangar, slip, mailbox, and so forth, at a given street address

## Relationships

- **Subclass of**: [AddressComponent](/concepts/fibo/FND/Places/Addresses/AddressComponent.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [SecondaryUnitDesignator](/concepts/fibo/FND/Places/Addresses/SecondaryUnitDesignator.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [SecondaryUnitIndicator](/concepts/fibo/FND/Places/Addresses/SecondaryUnitIndicator.md)

## Annotations

- **label**: secondary unit
- **definition**: address component that identifies an individual unit within a larger structure, such as an apartment, office, hangar, slip, mailbox, and so forth, at a given street address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
