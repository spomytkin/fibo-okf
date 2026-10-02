---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: board member
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that has fiduciary responsibility with respect to the organization, including but not limited to determining
      and executing corporate policy
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nc80669e32b564c12bf735c3dee7d641d
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nf3e60dd32b7346e28fa8bc9243ad8705
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: board member
type: Ontology Class
---

# board member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember>

## Definition

party that has fiduciary responsibility with respect to the organization, including but not limited to determining and executing corporate policy

## Relationships

- **Subclass of**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)
- **Subclass of**: [ResponsibleParty](<https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty>)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nc80669e32b564c12bf735c3dee7d641d`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nf3e60dd32b7346e28fa8bc9243ad8705`

## Annotations

- **label**: board member
- **definition**: party that has fiduciary responsibility with respect to the organization, including but not limited to determining and executing corporate policy

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
