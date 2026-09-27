---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity controlling party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that has the authority to control some legal entity
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This type of party is either asserted to be the case by the entity itself or some other party, or is determined
      through some analysis or calculation based on the available information about controlling interests.
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: It is assumed that since control follows from some form of ownership or contractual instrument, that the range
      of entities which may fulfil this party role is the same as that for entity ownership, namely a logical union of natural
      persons, legal persons and formal organizations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyOf
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: entity controlling party
type: Ontology Class
---

# entity controlling party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty>

## Definition

party that has the authority to control some legal entity

## Relationships

- **Subclass of**: [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)

## Constraints

- **[isControllingPartyOf](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyOf.md)**: some values from of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: entity controlling party
- **definition**: party that has the authority to control some legal entity
- **editorialNote**: This type of party is either asserted to be the case by the entity itself or some other party, or is determined through some analysis or calculation based on the available information about controlling interests.
- **scopeNote**: It is assumed that since control follows from some form of ownership or contractual instrument, that the range of entities which may fulfil this party role is the same as that for entity ownership, namely a logical union of natural persons, legal persons and formal organizations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
