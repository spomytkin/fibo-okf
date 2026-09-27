---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal entity identifier registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry for registering and maintaining information about business entities for a particular jurisdiction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LEI registry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistry
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: legal entity identifier registry
type: Ontology Class
---

# legal entity identifier registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistry>

## Definition

registry for registering and maintaining information about business entities for a particular jurisdiction

## Relationships

- **Subclass of**: [BusinessRegistry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [LegalEntityIdentifierRegistryEntry](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry.md)

## Annotations

- **label**: legal entity identifier registry
- **definition**: registry for registering and maintaining information about business entities for a particular jurisdiction
- **abbreviation**: LEI registry
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
