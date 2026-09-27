---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity legal form registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry for registering and maintaining information about the legal forms that are valid for business entities
      for a particular jurisdiction following the ISO 20275 standard
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ELF registry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistryEntry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistry
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: entity legal form registry
type: Ontology Class
---

# entity legal form registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistry>

## Definition

registry for registering and maintaining information about the legal forms that are valid for business entities for a particular jurisdiction following the ISO 20275 standard

## Relationships

- **Subclass of**: [Registry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [EntityLegalFormRegistryEntry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistryEntry.md)

## Annotations

- **label**: entity legal form registry
- **definition**: registry for registering and maintaining information about the legal forms that are valid for business entities for a particular jurisdiction following the ISO 20275 standard
- **abbreviation**: ELF registry
- **adaptedFrom**: https://www.gleif.org/en/about-lei/code-lists/iso-20275-entity-legal-forms-code-list

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
