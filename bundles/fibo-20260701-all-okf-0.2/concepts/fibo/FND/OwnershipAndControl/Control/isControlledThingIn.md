---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is controlled thing in
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the context of control in which something is being controlled
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
  inverse_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/involvesControlledThing.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/involvesControlledThing
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/undergoes
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledThingIn
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: is controlled thing in
type: Ontology Property
---

# is controlled thing in

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledThingIn>

## Definition

indicates the context of control in which something is being controlled

## Relationships

- **Domain**: [ControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md)
- **Inverse of**: [involvesControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/involvesControlledThing.md)
- **Range**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)
- **Subproperty of**: [undergoes](<https://www.omg.org/spec/Commons/PartiesAndSituations/undergoes>)

## Annotations

- **label**: is controlled thing in
- **definition**: indicates the context of control in which something is being controlled

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
