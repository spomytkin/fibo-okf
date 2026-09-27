---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: executive
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: person appointed and given the responsibility to manage the affairs of an organization and the authority to make
      decisions within specified role-specific boundaries
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Executive
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: executive
type: Ontology Class
---

# executive

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Executive>

## Definition

person appointed and given the responsibility to manage the affairs of an organization and the authority to make decisions within specified role-specific boundaries

## Relationships

- **Subclass of**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: executive
- **definition**: person appointed and given the responsibility to manage the affairs of an organization and the authority to make decisions within specified role-specific boundaries

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
