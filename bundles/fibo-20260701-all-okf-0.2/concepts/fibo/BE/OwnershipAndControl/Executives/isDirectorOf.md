---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is director of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the organization that the board member oversees
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/hasDirector.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasDirector
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isPartyControlling
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/isDirectorOf
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: is director of
type: Ontology Property
---

# is director of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/isDirectorOf>

## Definition

indicates the organization that the board member oversees

## Relationships

- **Domain**: [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)
- **Inverse of**: [hasDirector](/concepts/fibo/BE/OwnershipAndControl/Executives/hasDirector.md)
- **Range**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Subproperty of**: [isPartyControlling](/concepts/fibo/FND/OwnershipAndControl/Control/isPartyControlling.md)

## Annotations

- **label**: is director of
- **definition**: indicates the organization that the board member oversees

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
