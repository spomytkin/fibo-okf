---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: IBAN registration authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ISO 13616:2007, International Bank Account Number (IBAN) Registration Authority (RA) and financial service provider,
      appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO
      13616:2007, Financial services - International bank account number (IBAN)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.swift.com/standards/data-standards/iban
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
  - https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry.md
    predicate: https://www.omg.org/spec/Commons/Organizations/manages
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication.md
    predicate: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/IBANRegistrationAuthority
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: IBAN registration authority
type: Ontology Individual
---

# IBAN registration authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/IBANRegistrationAuthority>

## Definition

ISO 13616:2007, International Bank Account Number (IBAN) Registration Authority (RA) and financial service provider, appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 13616:2007, Financial services - International bank account number (IBAN)

## Relationships

- **Related to**: [BusinessIdentifierCodeRegistry](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BusinessIdentifierCodeRegistry.md)
- **Related to**: [SocietyForWorldwideInterbankFinancialTelecommunication](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SocietyForWorldwideInterbankFinancialTelecommunication.md)

## Annotations

- **label**: IBAN registration authority
- **definition**: ISO 13616:2007, International Bank Account Number (IBAN) Registration Authority (RA) and financial service provider, appointed by the International Standards Organization (ISO), that is the official registration authority (RA) for ISO 13616:2007, Financial services - International bank account number (IBAN)
- **adaptedFrom**: https://www.swift.com/standards/data-standards/iban

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
