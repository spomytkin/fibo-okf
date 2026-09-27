---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: examiner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party empowered as an official representative by a regulatory agency to investigate and review specified documents
      for accuracy and truthfulness
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Black's Law Dictionary, see http://thelawdictionary.org/examiner/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: EDM Council
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/BusinessAuthorizations/isAuthorizedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N329029ab45ec45faafcf6ec544473b94
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/Examiner
sources:
- id: fibo-source-ef717d20cc
  resource: references/fibo/FBC/FunctionalEntities/RegulatoryAgencies.rdf
  sha256: ef717d20cc3804b8cc9643a625bf716211db11cc374a524b54dd5ce7e70bf1db
  title: FIBO source FBC/FunctionalEntities/RegulatoryAgencies.rdf
title: examiner
type: Ontology Class
---

# examiner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/Examiner>

## Definition

party empowered as an official representative by a regulatory agency to investigate and review specified documents for accuracy and truthfulness

## Relationships

- **Subclass of**: [ResponsibleParty](<https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty>)

## Constraints

- **[isAuthorizedBy](<https://www.omg.org/spec/Commons/BusinessAuthorizations/isAuthorizedBy>)**: exact qualified cardinality 1 of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N329029ab45ec45faafcf6ec544473b94`

## Annotations

- **label**: examiner
- **definition**: party empowered as an official representative by a regulatory agency to investigate and review specified documents for accuracy and truthfulness
- **adaptedFrom**: Black's Law Dictionary, see http://thelawdictionary.org/examiner/
- **adaptedFrom**: EDM Council

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
