---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business identifier code registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry for registering and maintaining information about bank and other business identifier codes that conform
      to ISO 9362
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BIC registry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.swift.com/standards/data-standards/bic
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistrationAuthority.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistrationAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: business identifier code registry
type: Ontology Individual
---

# business identifier code registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry>

## Definition

registry for registering and maintaining information about bank and other business identifier codes that conform to ISO 9362

## Relationships

- **Related to**: [BusinessIdentifierCodeRegistrationAuthority](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistrationAuthority.md)

## Annotations

- **label**: business identifier code registry
- **definition**: registry for registering and maintaining information about bank and other business identifier codes that conform to ISO 9362
- **abbreviation**: BIC registry
- **adaptedFrom**: https://www.swift.com/standards/data-standards/bic

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
