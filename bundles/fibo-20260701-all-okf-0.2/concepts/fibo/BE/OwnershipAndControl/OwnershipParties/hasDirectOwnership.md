---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has direct ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a formal organization to the situation in which it is owned directly by another entity
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/experiences
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasDirectOwnership
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: has direct ownership
type: Ontology Property
---

# has direct ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasDirectOwnership>

## Definition

relates a formal organization to the situation in which it is owned directly by another entity

## Relationships

- **Inverse of**: [hasOwnedEntity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity.md)
- **Range**: [EntityOwnership](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md)
- **Subproperty of**: [experiences](<https://www.omg.org/spec/Commons/PartiesAndSituations/experiences>)

## Annotations

- **label**: has direct ownership
- **definition**: relates a formal organization to the situation in which it is owned directly by another entity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
