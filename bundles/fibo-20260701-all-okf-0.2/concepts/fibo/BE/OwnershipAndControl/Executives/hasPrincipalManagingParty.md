---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has principal managing party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a controlling party that is responsible for the management of daily business operations
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  inverse_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/isPrincipalPartyOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/isPrincipalPartyOf
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/PrincipalParty
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasPrincipalManagingParty
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: has principal managing party
type: Ontology Property
---

# has principal managing party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/hasPrincipalManagingParty>

## Definition

indicates a controlling party that is responsible for the management of daily business operations

## Relationships

- **Domain**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Inverse of**: [isPrincipalPartyOf](/concepts/fibo/BE/OwnershipAndControl/Executives/isPrincipalPartyOf.md)
- **Range**: [PrincipalParty](/concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md)
- **Subproperty of**: [hasControllingOrganizationMember](/concepts/fibo/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember.md)

## Annotations

- **label**: has principal managing party
- **definition**: indicates a controlling party that is responsible for the management of daily business operations

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
