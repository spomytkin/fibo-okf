---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: special purpose vehicle
  - language: fr-FR
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fonds commun de placement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity created to fulfill narrow, specific, and frequently temporary objectives
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SPE
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SPV
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A special purpose vehicle (SPV), also known as a special purpose entity (SPE), refers to a legal entity, typically
      a limited company or partnership, created to isolate a parent company from financial risk, including bankruptcy.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: special purpose entity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/hasIntendedLiquidationDate
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: fonds commun de placement
type: Ontology Class
---

# fonds commun de placement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle>

## Definition

legal entity created to fulfill narrow, specific, and frequently temporary objectives

## Relationships

- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Constraints

- **[hasIntendedLiquidationDate](/concepts/fibo/BE/LegalEntities/LegalPersons/hasIntendedLiquidationDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en-US): special purpose vehicle
- **label** (fr-FR): fonds commun de placement
- **definition** (en): legal entity created to fulfill narrow, specific, and frequently temporary objectives
- **abbreviation** (en): SPE
- **abbreviation** (en): SPV
- **explanatoryNote** (en): A special purpose vehicle (SPV), also known as a special purpose entity (SPE), refers to a legal entity, typically a limited company or partnership, created to isolate a parent company from financial risk, including bankruptcy.
- **synonym** (en): special purpose entity

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
