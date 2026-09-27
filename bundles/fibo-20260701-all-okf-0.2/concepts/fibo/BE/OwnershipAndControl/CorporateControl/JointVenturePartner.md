---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: joint venture partner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that shares capital, technology, human resources, risks, and benefits of an entity under shared control
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/JointVenture
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyOf
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/JointVenturePartner
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: joint venture partner
type: Ontology Class
---

# joint venture partner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/JointVenturePartner>

## Definition

party that shares capital, technology, human resources, risks, and benefits of an entity under shared control

## Relationships

- **Subclass of**: [EntityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)

## Constraints

- **[isControllingPartyOf](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyOf.md)**: some values from of type [JointVenture](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/JointVenture.md)

## Annotations

- **label**: joint venture partner
- **definition**: party that shares capital, technology, human resources, risks, and benefits of an entity under shared control

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
