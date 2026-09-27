---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is principal party of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a legal entity (controlled party) over which a principal has some measure of control
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/PrincipalParty
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isControllingMemberOf
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/isPrincipalPartyOf
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: is principal party of
type: Ontology Property
---

# is principal party of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/isPrincipalPartyOf>

## Definition

identifies a legal entity (controlled party) over which a principal has some measure of control

## Relationships

- **Domain**: [PrincipalParty](/concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md)
- **Range**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Subproperty of**: [isControllingMemberOf](/concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md)

## Annotations

- **label**: is principal party of
- **definition**: identifies a legal entity (controlled party) over which a principal has some measure of control

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
