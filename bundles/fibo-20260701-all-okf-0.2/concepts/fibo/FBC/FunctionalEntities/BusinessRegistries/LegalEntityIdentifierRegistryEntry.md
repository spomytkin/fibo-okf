---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal entity identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a legal entity identifier registry that conforms to ISO 17442 and the Global Legal Entity Identifier Foundation
      (GLEIF) Common Data Format (CDF)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LEI registry entry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasManagingLocalOperatingUnit
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationAuthority
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevel
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: legal entity identifier registry entry
type: Ontology Class
---

# legal entity identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry>

## Definition

entry in a legal entity identifier registry that conforms to ISO 17442 and the Global Legal Entity Identifier Foundation (GLEIF) Common Data Format (CDF)

## Relationships

- **Subclass of**: [BusinessRegistryEntry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md)

## Constraints

- **[hasManagingLocalOperatingUnit](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasManagingLocalOperatingUnit.md)**: all values from of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- **[hasRegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus.md)**: some values from of type [RegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
- **[hasValidationAuthority](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasValidationAuthority.md)**: min qualified cardinality 0 of type [BusinessRegistrationAuthority](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)
- **[hasValidationLevel](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel.md)**: some values from of type [EntityValidationLevel](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevel.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)

## Annotations

- **label**: legal entity identifier registry entry
- **definition**: entry in a legal entity identifier registry that conforms to ISO 17442 and the Global Legal Entity Identifier Foundation (GLEIF) Common Data Format (CDF)
- **abbreviation**: LEI registry entry
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
