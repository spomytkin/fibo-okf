---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has owned entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a formal organization, including potentially a sole proprietorship, that is owned by a legal person
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isExperiencedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: has owned entity
type: Ontology Property
---

# has owned entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity>

## Definition

indicates a formal organization, including potentially a sole proprietorship, that is owned by a legal person

## Relationships

- **Domain**: [EntityOwnership](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md)
- **Subproperty of**: [isExperiencedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isExperiencedBy>)

## Annotations

- **label**: has owned entity
- **definition**: indicates a formal organization, including potentially a sole proprietorship, that is owned by a legal person

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
