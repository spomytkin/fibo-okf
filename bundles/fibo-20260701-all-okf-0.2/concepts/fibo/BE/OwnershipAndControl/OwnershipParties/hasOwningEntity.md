---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has owning entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a party that owns a formal organization
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasActiveParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: has owning entity
type: Ontology Property
---

# has owning entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity>

## Definition

indicates a party that owns a formal organization

## Relationships

- **Domain**: [EntityOwnership](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md)
- **Range**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **Subproperty of**: [hasActiveParty](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasActiveParty>)

## Annotations

- **label**: has owning entity
- **definition**: indicates a party that owns a formal organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
