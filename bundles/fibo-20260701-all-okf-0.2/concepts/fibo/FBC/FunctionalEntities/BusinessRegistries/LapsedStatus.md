---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lapsed status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: status indicating that the registration that has not been renewed by the specified renewal date and is not known
      by public sources to have ceased operation as of the last update
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: LAPSED
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LapsedStatus
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: lapsed status
type: Ontology Individual
---

# lapsed status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LapsedStatus>

## Definition

status indicating that the registration that has not been renewed by the specified renewal date and is not known by public sources to have ceased operation as of the last update

## Annotations

- **label**: lapsed status
- **definition**: status indicating that the registration that has not been renewed by the specified renewal date and is not known by public sources to have ceased operation as of the last update
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **hasTag**: LAPSED

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
