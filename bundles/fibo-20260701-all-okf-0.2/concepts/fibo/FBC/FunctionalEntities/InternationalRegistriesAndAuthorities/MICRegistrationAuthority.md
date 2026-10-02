---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MIC registration authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ISO 10383, Market Identifier Code (MIC) Registration Authority (RA) and financial service provider, appointed by
      the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 10383, Codes
      for exchanges and market identification (MIC)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MIC RA
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.anna-web.org/standards/mic-iso-10383/
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/10383/iso-10383-market-identifier-codes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: ISO 10383 Registration Authority
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry.md
    predicate: https://www.omg.org/spec/Commons/Organizations/manages
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MICRegistrationAuthority
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: MIC registration authority
type: Ontology Individual
---

# MIC registration authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MICRegistrationAuthority>

## Definition

ISO 10383, Market Identifier Code (MIC) Registration Authority (RA) and financial service provider, appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 10383, Codes for exchanges and market identification (MIC)

## Relationships

- **Related to**: [MarketIdentifierCodeRegistry](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry.md)
- **Related to**: [SocietyForWorldwideInterbankFinancialTelecommunication](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication.md)

## Annotations

- **label**: MIC registration authority
- **definition**: ISO 10383, Market Identifier Code (MIC) Registration Authority (RA) and financial service provider, appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 10383, Codes for exchanges and market identification (MIC)
- **abbreviation**: MIC RA
- **adaptedFrom**: https://www.anna-web.org/standards/mic-iso-10383/
- **adaptedFrom**: https://www.iso20022.org/10383/iso-10383-market-identifier-codes
- **synonym**: ISO 10383 Registration Authority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
