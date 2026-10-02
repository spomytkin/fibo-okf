---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business registration authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration authority that is responsible for maintaining a registry of business entities
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/gleif-registration-authorities-list
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A business registry may include any government-managed registry for registering a business, such as a state department
      of corporations in the US, as well as other registries such as a local operating unit (LOU) for registration of legal
      entity identifiers (LEIs). Any sanctioned registration authority as defined by the Registration Authorities List, published
      by GLEIF, is a business registration authority in this sense.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/registers
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registrar
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: business registration authority
type: Ontology Class
---

# business registration authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority>

## Definition

registration authority that is responsible for maintaining a registry of business entities

## Relationships

- **Subclass of**: [Registrar](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registrar>)
- **Subclass of**: [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)

## Constraints

- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [BusinessRegistry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md)
- **[registers](<https://www.omg.org/spec/Commons/RegistrationAuthorities/registers>)**: some values from of type [RegistrationIdentifier](/concepts/fibo/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md)

## Annotations

- **label**: business registration authority
- **definition**: registration authority that is responsible for maintaining a registry of business entities
- **adaptedFrom**: https://www.gleif.org/en/about-lei/gleif-registration-authorities-list
- **explanatoryNote**: A business registry may include any government-managed registry for registering a business, such as a state department of corporations in the US, as well as other registries such as a local operating unit (LOU) for registration of legal entity identifiers (LEIs). Any sanctioned registration authority as defined by the Registration Authorities List, published by GLEIF, is a business registration authority in this sense.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
