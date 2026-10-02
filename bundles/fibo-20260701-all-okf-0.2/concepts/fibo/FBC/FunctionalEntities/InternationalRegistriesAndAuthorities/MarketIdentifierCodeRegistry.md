---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market identifier code registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry for registering and maintaining information for market identifier codes that conform to ISO 10383
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MIC registry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/10383/iso-10383-market-identifier-codes
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MICRegistrationAuthority.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MICRegistrationAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: market identifier code registry
type: Ontology Individual
---

# market identifier code registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry>

## Definition

registry for registering and maintaining information for market identifier codes that conform to ISO 10383

## Relationships

- **Related to**: [MICRegistrationAuthority](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MICRegistrationAuthority.md)

## Annotations

- **label**: market identifier code registry
- **definition**: registry for registering and maintaining information for market identifier codes that conform to ISO 10383
- **abbreviation**: MIC registry
- **adaptedFrom**: https://www.iso20022.org/10383/iso-10383-market-identifier-codes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
