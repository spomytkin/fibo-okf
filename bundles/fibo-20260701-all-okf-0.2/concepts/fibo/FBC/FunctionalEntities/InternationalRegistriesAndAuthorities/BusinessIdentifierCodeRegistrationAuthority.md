---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Business Identifier Code registration authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration authority and financial service provider, appointed by the International Standards Organization (ISO),
      that is the official registration authority (RA) for ISO 9362, Banking - Banking telecommunication messages - Business
      identifier code (BIC)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BIC RA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BIC registration authority
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.swift.com/standards/data-standards/bic
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: BIC code registrar
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry.md
    predicate: https://www.omg.org/spec/Commons/Organizations/manages
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistrationAuthority
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: Business Identifier Code registration authority
type: Ontology Individual
---

# Business Identifier Code registration authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistrationAuthority>

## Definition

registration authority and financial service provider, appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 9362, Banking - Banking telecommunication messages - Business identifier code (BIC)

## Relationships

- **Related to**: [BusinessIdentifierCodeRegistry](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry.md)
- **Related to**: [SocietyForWorldwideInterbankFinancialTelecommunication](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication.md)

## Annotations

- **label**: Business Identifier Code registration authority
- **definition**: registration authority and financial service provider, appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 9362, Banking - Banking telecommunication messages - Business identifier code (BIC)
- **abbreviation**: BIC RA
- **abbreviation**: BIC registration authority
- **adaptedFrom**: https://www.swift.com/standards/data-standards/bic
- **synonym**: BIC code registrar

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
