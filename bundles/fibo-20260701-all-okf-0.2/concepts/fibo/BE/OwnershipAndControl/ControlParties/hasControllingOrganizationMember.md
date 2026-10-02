---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has controlling organization member
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a controlled party to a controlling member of the organization
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isControllingMemberOf
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
title: has controlling organization member
type: Ontology Property
---

# has controlling organization member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember>

## Definition

relates a controlled party to a controlling member of the organization

## Relationships

- **Domain**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Inverse of**: [isControllingMemberOf](/concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md)
- **Range**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)
- **Subproperty of**: [hasControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md)

## Annotations

- **label**: has controlling organization member
- **definition**: relates a controlled party to a controlling member of the organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
