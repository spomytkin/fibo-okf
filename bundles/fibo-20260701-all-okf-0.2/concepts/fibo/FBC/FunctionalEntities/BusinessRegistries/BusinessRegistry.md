---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry for registering and maintaining information about business entities
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/gleif-registration-authorities-list
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistryName
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: business registry
type: Ontology Class
---

# business registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry>

## Definition

registry for registering and maintaining information about business entities

## Relationships

- **Subclass of**: [Registry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry>)

## Constraints

- **[hasRegistryName](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistryName.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [BusinessRegistryEntry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: exact qualified cardinality 1 of type [BusinessRegistrationAuthority](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)

## Annotations

- **label**: business registry
- **definition**: registry for registering and maintaining information about business entities
- **adaptedFrom**: https://www.gleif.org/en/about-lei/gleif-registration-authorities-list

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
