---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has entity expiration reason
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the reason that an entity ceased to exist (i.e., disolved, merged with another entity, etc.)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityExpirationReason.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityExpirationReason
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Designators/isSignifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasEntityExpirationReason
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has entity expiration reason
type: Ontology Property
---

# has entity expiration reason

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasEntityExpirationReason>

## Definition

indicates the reason that an entity ceased to exist (i.e., disolved, merged with another entity, etc.)

## Relationships

- **Range**: [EntityExpirationReason](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityExpirationReason.md)
- **Subproperty of**: [isSignifiedBy](<https://www.omg.org/spec/Commons/Designators/isSignifiedBy>)

## Annotations

- **label**: has entity expiration reason
- **definition**: indicates the reason that an entity ceased to exist (i.e., disolved, merged with another entity, etc.)
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
