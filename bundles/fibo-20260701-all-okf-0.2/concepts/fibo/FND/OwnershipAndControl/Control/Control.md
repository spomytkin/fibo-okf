---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: control
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation in which some party has the power to direct or strongly influence the direction of the management and
      policies related to something
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Control may be direct (explicit) or indirect (implicit), derived through ownership of voting shares, beneficial
      ownership, other ownership relations, through provisions of a contract, or otherwise.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasPartyInControl
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/involvesControlledThing
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: control
type: Ontology Class
---

# control

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control>

## Definition

situation in which some party has the power to direct or strongly influence the direction of the management and policies related to something

## Relationships

- **Subclass of**: [Situation](<https://www.omg.org/spec/Commons/PartiesAndSituations/Situation>)

## Constraints

- **[hasPartyInControl](/concepts/fibo/FND/OwnershipAndControl/Control/hasPartyInControl.md)**: some values from of type [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)
- **[involvesControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/involvesControlledThing.md)**: some values from of type [ControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md)

## Annotations

- **label**: control
- **definition**: situation in which some party has the power to direct or strongly influence the direction of the management and policies related to something
- **explanatoryNote**: Control may be direct (explicit) or indirect (implicit), derived through ownership of voting shares, beneficial ownership, other ownership relations, through provisions of a contract, or otherwise.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
