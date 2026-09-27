---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has secondary unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies an individual unit within a larger structure, such as an apartment, office, hangar, slip, mailbox, and
      so forth, at a given street address
  domain:
  - concept: /concepts/fibo/FND/Places/Addresses/StreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/SecondaryUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnit
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/comprises
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasSecondaryUnit
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
title: has secondary unit
type: Ontology Property
---

# has secondary unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasSecondaryUnit>

## Definition

specifies an individual unit within a larger structure, such as an apartment, office, hangar, slip, mailbox, and so forth, at a given street address

## Relationships

- **Domain**: [StreetAddress](/concepts/fibo/FND/Places/Addresses/StreetAddress.md)
- **Range**: [SecondaryUnit](/concepts/fibo/FND/Places/Addresses/SecondaryUnit.md)
- **Subproperty of**: [comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)

## Annotations

- **label**: has secondary unit
- **definition**: specifies an individual unit within a larger structure, such as an apartment, office, hangar, slip, mailbox, and so forth, at a given street address

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
