---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Financial Instrument Global Identifier (FIGI) registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a Financial Instrument Global Identifier (FIGI) registry
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FIGI registry entry
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.omg.org/spec/FIGI
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: Ndd471165ad364f0ba865de278d42c8a5
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistryEntry
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Financial Instrument Global Identifier (FIGI) registry entry
type: Ontology Class
---

# Financial Instrument Global Identifier (FIGI) registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistryEntry>

## Definition

entry in a Financial Instrument Global Identifier (FIGI) registry

## Relationships

- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [FinancialInstrumentGlobalIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifier.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/FinancialInstrumentGlobalIdentifierRegistry`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from value `Ndd471165ad364f0ba865de278d42c8a5`

## Annotations

- **label**: Financial Instrument Global Identifier (FIGI) registry entry
- **definition**: entry in a Financial Instrument Global Identifier (FIGI) registry
- **abbreviation**: FIGI registry entry
- **adaptedFrom**: https://www.omg.org/spec/FIGI

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
