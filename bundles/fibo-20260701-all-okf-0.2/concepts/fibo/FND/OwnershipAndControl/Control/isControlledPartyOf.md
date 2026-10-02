---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is controlled party of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a controlling party that has some amount of authority or influence over it
  range:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isDirectlyAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledPartyOf
sources:
- id: fibo-source-b62f5055c5
  resource: references/fibo/FND/OwnershipAndControl/Control.rdf
  sha256: b62f5055c539290530c387d27526ed613d4570b7c04105acfa6a5bc91f8e7569
  title: FIBO source FND/OwnershipAndControl/Control.rdf
title: is controlled party of
type: Ontology Property
---

# is controlled party of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControlledPartyOf>

## Definition

indicates a controlling party that has some amount of authority or influence over it

## Relationships

- **Range**: [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)
- **Subproperty of**: [isDirectlyAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isDirectlyAffectedBy>)

## Annotations

- **label**: is controlled party of
- **definition**: indicates a controlling party that has some amount of authority or influence over it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
