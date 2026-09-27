---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: controlled thing
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: something over which some party exercises some form of control with respect to some situation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasControllingParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledThingIn
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isInitiallyControlledOn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Undergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: controlled thing
type: Ontology Class
---

# controlled thing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing>

## Definition

something over which some party exercises some form of control with respect to some situation

## Relationships

- **Subclass of**: [Undergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/Undergoer>)

## Constraints

- **[hasControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md)**: some values from of type [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)
- **[isControlledThingIn](/concepts/fibo/FND/OwnershipAndControl/Control/isControlledThingIn.md)**: some values from of type [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)
- **[isInitiallyControlledOn](/concepts/fibo/FND/OwnershipAndControl/Control/isInitiallyControlledOn.md)**: exact qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: controlled thing
- **definition**: something over which some party exercises some form of control with respect to some situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
