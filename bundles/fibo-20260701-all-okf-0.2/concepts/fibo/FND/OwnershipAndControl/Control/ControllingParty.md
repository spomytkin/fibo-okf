---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: controlling party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: actor that exercises some form of control in the context of some situation
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: At this level of abstraction it is not defined whether the control is some degree of controlling interest, or some
      level of actual control (asserted or calculated) in some entity.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isPartyControlling
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Actor
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: controlling party
type: Ontology Class
---

# controlling party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty>

## Definition

actor that exercises some form of control in the context of some situation

## Relationships

- **Subclass of**: [Actor](<https://www.omg.org/spec/Commons/PartiesAndSituations/Actor>)

## Constraints

- **[isControllingPartyIn](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyIn.md)**: some values from of type [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)
- **[isPartyControlling](/concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md)**: some values from of type [ControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md)

## Annotations

- **label**: controlling party
- **definition**: actor that exercises some form of control in the context of some situation
- **editorialNote**: At this level of abstraction it is not defined whether the control is some degree of controlling interest, or some level of actual control (asserted or calculated) in some entity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
