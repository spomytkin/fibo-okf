---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited liability company member
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: owner of an interest in a limited liability company
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isControllingMemberOf
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N28184a1a10284439b24a8d4cf224b810
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyMember
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: limited liability company member
type: Ontology Class
---

# limited liability company member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyMember>

## Definition

owner of an interest in a limited liability company

## Relationships

- **Subclass of**: [DeJureControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- **Subclass of**: [EntityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)
- **Subclass of**: [EntityOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isControllingMemberOf](/concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md)**: min qualified cardinality 0
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N28184a1a10284439b24a8d4cf224b810`

## Annotations

- **label**: limited liability company member
- **definition**: owner of an interest in a limited liability company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
