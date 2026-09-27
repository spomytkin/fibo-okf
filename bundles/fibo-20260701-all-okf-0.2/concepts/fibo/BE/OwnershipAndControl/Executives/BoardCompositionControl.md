---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: board composition control
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: situation in which a voting shareholder, entity owner, or some other party in the case of a not-for-profit organization,
      appoints and/or nominates someone to the board of directors of an organization for some period of time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasPartyInControl
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/involvesControlledThing
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/Control.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardCompositionControl
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: board composition control
type: Ontology Class
---

# board composition control

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardCompositionControl>

## Definition

situation in which a voting shareholder, entity owner, or some other party in the case of a not-for-profit organization, appoints and/or nominates someone to the board of directors of an organization for some period of time

## Relationships

- **Subclass of**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control/Control.md)

## Constraints

- **[hasPartyInControl](/concepts/fibo/FND/OwnershipAndControl/Control/hasPartyInControl.md)**: min qualified cardinality 0
- **[involvesControlledThing](/concepts/fibo/FND/OwnershipAndControl/Control/involvesControlledThing.md)**: some values from of type [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)

## Annotations

- **label**: board composition control
- **definition**: situation in which a voting shareholder, entity owner, or some other party in the case of a not-for-profit organization, appoints and/or nominates someone to the board of directors of an organization for some period of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
