---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has director
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a member of the board of directors of the organization
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasDirector
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: has director
type: Ontology Property
---

# has director

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasDirector>

## Definition

indicates a member of the board of directors of the organization

## Relationships

- **Domain**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Range**: [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)
- **Subproperty of**: [hasControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md)

## Annotations

- **label**: has director
- **definition**: indicates a member of the board of directors of the organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
