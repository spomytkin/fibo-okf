---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is party controlling
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates something controlled that a controlling party has some amount of authority or influence over
  domain:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
  inverse_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasControllingParty
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isPartyControlling
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: is party controlling
type: Ontology Property
---

# is party controlling

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isPartyControlling>

## Definition

indicates something controlled that a controlling party has some amount of authority or influence over

## Relationships

- **Domain**: [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)
- **Inverse of**: [hasControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md)
- **Range**: [ControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/ControlledThing.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: is party controlling
- **definition**: indicates something controlled that a controlling party has some amount of authority or influence over

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
