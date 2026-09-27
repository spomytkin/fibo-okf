---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: local operating unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registrar that is authorized by the Global LEI Foundation to issue legal entity identifiers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LOU
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: LOUs supply registration, renewal and other services, and act as the primary interface for legal entities wishing
      to obtain an LEI.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/registers
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registrar
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LocalOperatingUnit
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: local operating unit
type: Ontology Class
---

# local operating unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LocalOperatingUnit>

## Definition

registrar that is authorized by the Global LEI Foundation to issue legal entity identifiers

## Relationships

- **Subclass of**: [Registrar](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registrar>)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- **[registers](<https://www.omg.org/spec/Commons/RegistrationAuthorities/registers>)**: some values from of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)

## Annotations

- **label**: local operating unit
- **definition**: registrar that is authorized by the Global LEI Foundation to issue legal entity identifiers
- **abbreviation**: LOU
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **explanatoryNote**: LOUs supply registration, renewal and other services, and act as the primary interface for legal entities wishing to obtain an LEI.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
