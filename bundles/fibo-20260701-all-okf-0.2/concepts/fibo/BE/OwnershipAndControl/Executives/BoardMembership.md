---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: board membership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation relating an individual member of the board of directors to the organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasPartyInControl
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/involvesControlledThing
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMembership
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: board membership
type: Ontology Class
---

# board membership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMembership>

## Definition

situation relating an individual member of the board of directors to the organization

## Relationships

- **Subclass of**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)

## Constraints

- **[hasPartyInControl](/concepts/fibo/FND/OwnershipAndControl/Control/hasPartyInControl.md)**: some values from of type [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)
- **[involvesControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/involvesControlledThing.md)**: some values from of type [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)

## Annotations

- **label**: board membership
- **definition**: situation relating an individual member of the board of directors to the organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
