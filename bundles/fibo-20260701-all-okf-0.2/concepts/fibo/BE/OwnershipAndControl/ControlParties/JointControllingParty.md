---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: joint controlling party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that collectively has the authority to control the affairs of some business organization
  disjoint_with:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/SoleControllingParty.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/SoleControllingParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControllingAlliance
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/JointControllingParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: joint controlling party
type: Ontology Class
---

# joint controlling party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/JointControllingParty>

## Definition

party that collectively has the authority to control the affairs of some business organization

## Relationships

- **Subclass of**: [EntityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)

## Constraints

- **Disjoint with**: [SoleControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/SoleControllingParty.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [ControllingAlliance](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControllingAlliance.md)

## Annotations

- **label**: joint controlling party
- **definition**: party that collectively has the authority to control the affairs of some business organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
