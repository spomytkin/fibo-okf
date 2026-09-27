---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: individual investor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investor that is a person, rather than an organization, who may or may not be considered a qualified investor from
      a legal perspective
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/IndividualInvestor
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: individual investor
type: Ontology Class
---

# individual investor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/IndividualInvestor>

## Definition

investor that is a person, rather than an organization, who may or may not be considered a qualified investor from a legal perspective

## Relationships

- **Subclass of**: [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: individual investor
- **definition**: investor that is a person, rather than an organization, who may or may not be considered a qualified investor from a legal perspective

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
