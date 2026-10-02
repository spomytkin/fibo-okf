---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: authorized individual
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role of an individual that has been given the responsibility to act on behalf of another party under some set of
      guidelines
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/AuthorizedIndividual
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: authorized individual
type: Ontology Class
---

# authorized individual

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/AuthorizedIndividual>

## Definition

role of an individual that has been given the responsibility to act on behalf of another party under some set of guidelines

## Relationships

- **Subclass of**: [ResponsibleParty](<https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: authorized individual
- **definition**: role of an individual that has been given the responsibility to act on behalf of another party under some set of guidelines

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
