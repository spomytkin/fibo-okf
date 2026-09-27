---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has registry name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: denotes a name for the registry, for example, for a business registry in which a business registration identifier
      for the legal entity is registered
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/hasTextualName
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistryName
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has registry name
type: Ontology Property
---

# has registry name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistryName>

## Definition

denotes a name for the registry, for example, for a business registry in which a business registration identifier for the legal entity is registered

## Relationships

- **Domain**: [Registry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry>)
- **Subproperty of**: [hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)

## Annotations

- **label**: has registry name
- **definition**: denotes a name for the registry, for example, for a business registry in which a business registration identifier for the legal entity is registered
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
