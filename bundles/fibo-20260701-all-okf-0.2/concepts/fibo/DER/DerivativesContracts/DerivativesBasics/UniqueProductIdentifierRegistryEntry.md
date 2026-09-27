---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unique product identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a unique product identifier registry
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Reference Data Library (RDL) is a set of reference data elements, together with their values, which is properly
      organized and maintained by the UPI service provider. The library associates UPI codes with the values of the reference
      data elements characterizing the product. Each entry in the library (the registry entry) contains a minimum number of
      elements as defined in the ISO standard, and may be extended by the service provider.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierReferenceDataLibrary
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierRegistryEntry
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: unique product identifier registry entry
type: Ontology Class
---

# unique product identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierRegistryEntry>

## Definition

entry in a unique product identifier registry

## Relationships

- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [UniqueProductIdentifier](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifier.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/UniqueProductIdentifierReferenceDataLibrary`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from of type [OverTheCounterDerivativeInstrument](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)

## Annotations

- **label**: unique product identifier registry entry
- **definition**: entry in a unique product identifier registry
- **explanatoryNote**: The Reference Data Library (RDL) is a set of reference data elements, together with their values, which is properly organized and maintained by the UPI service provider. The library associates UPI codes with the values of the reference data elements characterizing the product. Each entry in the library (the registry entry) contains a minimum number of elements as defined in the ISO standard, and may be extended by the service provider.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
