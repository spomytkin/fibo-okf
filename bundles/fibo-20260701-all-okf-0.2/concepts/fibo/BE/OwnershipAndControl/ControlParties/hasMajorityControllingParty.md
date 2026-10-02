---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has majority controlling party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a party that owns a controlling stake (over 50 percent) in the entity
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/MajorityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/MajorityControllingParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/isControlledPartyOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledPartyOf
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasMajorityControllingParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: has majority controlling party
type: Ontology Property
---

# has majority controlling party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasMajorityControllingParty>

## Definition

indicates a party that owns a controlling stake (over 50 percent) in the entity

## Relationships

- **Domain**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Range**: [MajorityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/MajorityControllingParty.md)
- **Subproperty of**: [isControlledPartyOf](/concepts/fibo/FND/OwnershipAndControl/Control/isControlledPartyOf.md)

## Annotations

- **label**: has majority controlling party
- **definition**: indicates a party that owns a controlling stake (over 50 percent) in the entity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
