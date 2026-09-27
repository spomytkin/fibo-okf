---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument global identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument identifier that is defined as specified in the Object Management Group (OMG) Financial Instrument
      Global Identifier (FIGI) Specification
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FIGI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.omg.org/spec/FIGI
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The development of the Financial Instrument Global Identifier (FIGI) originated from a need for a standard methodology
      to bridge across multiple identification systems for financial instruments. Without prejudice against any existing symbol-based
      solutions, or any question of the validity of one system over the other, the FIGI standard utilizes a metadata driven
      approach to enable the unique and persistent identification of financial instruments. While in most cases, a FIGI uniquely
      identifies a security, there are situations outside of the U.S. where it instead identifies a listing for a security,
      similar to a ticker symbol.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierScheme
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
    value: N5602da658ef44a3ca692e734b9dcf3fc
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifier
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: financial instrument global identifier
type: Ontology Class
---

# financial instrument global identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifier>

## Definition

financial instrument identifier that is defined as specified in the Object Management Group (OMG) Financial Instrument Global Identifier (FIGI) Specification

## Relationships

- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierScheme`
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from value `N5602da658ef44a3ca692e734b9dcf3fc`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/BloombergLP`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry`

## Annotations

- **label**: financial instrument global identifier
- **definition**: financial instrument identifier that is defined as specified in the Object Management Group (OMG) Financial Instrument Global Identifier (FIGI) Specification
- **abbreviation**: FIGI
- **adaptedFrom**: https://www.omg.org/spec/FIGI
- **explanatoryNote**: The development of the Financial Instrument Global Identifier (FIGI) originated from a need for a standard methodology to bridge across multiple identification systems for financial instruments. Without prejudice against any existing symbol-based solutions, or any question of the validity of one system over the other, the FIGI standard utilizes a metadata driven approach to enable the unique and persistent identification of financial instruments. While in most cases, a FIGI uniquely identifies a security, there are situations outside of the U.S. where it instead identifies a listing for a security, similar to a ticker symbol.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
