---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business register identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity
      Identifier Foundation (GLEIF) registration authorities list
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/gleif-registration-authorities-list
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegisterIdentifier
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: business register identifier
type: Ontology Class
---

# business register identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegisterIdentifier>

## Definition

identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity Identifier Foundation (GLEIF) registration authorities list

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [BusinessRegistry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from of type [BusinessRegistrationAuthority](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)

## Annotations

- **label**: business register identifier
- **definition**: identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity Identifier Foundation (GLEIF) registration authorities list
- **adaptedFrom**: https://www.gleif.org/en/about-lei/gleif-registration-authorities-list

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
