---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: involves controlled thing
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates something controlled in the context of a control situation
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/involvesControlledThing
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: involves controlled thing
type: Ontology Property
---

# involves controlled thing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/involvesControlledThing>

## Definition

indicates something controlled in the context of a control situation

## Relationships

- **Domain**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)
- **Range**: [ControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md)
- **Subproperty of**: [hasUndergoer](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasUndergoer>)

## Annotations

- **label**: involves controlled thing
- **definition**: indicates something controlled in the context of a control situation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
