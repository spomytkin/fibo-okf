---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: ISO 4914:2021(en), Financial services - Unique product identifier (UPI)
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unique product identifier service provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: organization designated by an external body of financial regulators to assign UPIs and operate a UPI reference
      data library
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: At the time of publication of the ISO 4914 standard, there was only one such provider, the Regulatory Oversight
      Committee, confirmed by the Financial Stability Board as the International Governance Body for globally harmonised identifiers
      used to track OTC derivatives transactions.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: UPI service provider
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/registers
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: unique product identifier service provider
type: Ontology Class
---

# unique product identifier service provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierServiceProvider>

## Definition

organization designated by an external body of financial regulators to assign UPIs and operate a UPI reference data library

## Relationships

- **Subclass of**: [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)

## Constraints

- **[registers](<https://www.omg.org/spec/Commons/RegistrationAuthorities/registers>)**: min qualified cardinality 0 of type [UniqueProductIdentifier](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier.md)

## Annotations

- **source**: ISO 4914:2021(en), Financial services - Unique product identifier (UPI)
- **label**: unique product identifier service provider
- **definition**: organization designated by an external body of financial regulators to assign UPIs and operate a UPI reference data library
- **scopeNote**: At the time of publication of the ISO 4914 standard, there was only one such provider, the Regulatory Oversight Committee, confirmed by the Financial Stability Board as the International Governance Body for globally harmonised identifiers used to track OTC derivatives transactions.
- **abbreviation**: UPI service provider

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
