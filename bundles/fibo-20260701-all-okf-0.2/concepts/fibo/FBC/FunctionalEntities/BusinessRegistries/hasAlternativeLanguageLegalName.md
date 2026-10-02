---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has alternative language legal name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: denotes a registered legal name for the entity in an alternative language used in the legal jurisdiction in which
      the entity is registered
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Relations/Relations/hasLegalName.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasAlternativeLanguageLegalName
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has alternative language legal name
type: Ontology Property
---

# has alternative language legal name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasAlternativeLanguageLegalName>

## Definition

denotes a registered legal name for the entity in an alternative language used in the legal jurisdiction in which the entity is registered

## Relationships

- **Subproperty of**: [hasLegalName](/concepts/fibo/FND/Relations/Relations/hasLegalName.md)

## Annotations

- **label**: has alternative language legal name
- **definition**: denotes a registered legal name for the entity in an alternative language used in the legal jurisdiction in which the entity is registered
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
