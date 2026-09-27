---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has validation authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the business registration authority for the legal entity, used by the Local Operating Unit (LOU) as
      the basis for validation, as defined in the GLEIF Registration Authorities List
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationAuthority
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has validation authority
type: Ontology Property
---

# has validation authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationAuthority>

## Definition

identifies the business registration authority for the legal entity, used by the Local Operating Unit (LOU) as the basis for validation, as defined in the GLEIF Registration Authorities List

## Relationships

- **Range**: [BusinessRegistrationAuthority](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)
- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)

## Annotations

- **label**: has validation authority
- **definition**: identifies the business registration authority for the legal entity, used by the Local Operating Unit (LOU) as the basis for validation, as defined in the GLEIF Registration Authorities List
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
