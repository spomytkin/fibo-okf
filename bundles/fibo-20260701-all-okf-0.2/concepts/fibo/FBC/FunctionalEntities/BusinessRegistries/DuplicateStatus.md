---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: duplicate status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: status indicating that the registration was determined to be a duplicate registration of the same entity as another
      registration; duplicate status is assigned to the non-surviving registration (i.e. the identifier that should no longer
      be used)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: DUPLICATE
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/DuplicateStatus
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: duplicate status
type: Ontology Individual
---

# duplicate status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/DuplicateStatus>

## Definition

status indicating that the registration was determined to be a duplicate registration of the same entity as another registration; duplicate status is assigned to the non-surviving registration (i.e. the identifier that should no longer be used)

## Annotations

- **label**: duplicate status
- **definition**: status indicating that the registration was determined to be a duplicate registration of the same entity as another registration; duplicate status is assigned to the non-surviving registration (i.e. the identifier that should no longer be used)
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **hasTag**: DUPLICATE

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
