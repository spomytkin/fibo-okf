---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: signatory
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: responsible party authorized to sign agreements on behalf of themselves, another person, or an organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Na7a6789c358c45faa3d8284901bf17e1
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/AuthorizedIndividual.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/AuthorizedIndividual
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Signatory
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: signatory
type: Ontology Class
---

# signatory

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Signatory>

## Definition

responsible party authorized to sign agreements on behalf of themselves, another person, or an organization

## Relationships

- **Subclass of**: [AuthorizedIndividual](/concepts/fibo/BE/OwnershipAndControl/Executives/AuthorizedIndividual.md)
- **Subclass of**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Na7a6789c358c45faa3d8284901bf17e1`

## Annotations

- **label**: signatory
- **definition**: responsible party authorized to sign agreements on behalf of themselves, another person, or an organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
