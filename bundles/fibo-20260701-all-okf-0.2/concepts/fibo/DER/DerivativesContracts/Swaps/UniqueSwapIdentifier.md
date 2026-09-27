---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unique swap identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier for a swap that is used in recordkeeping and swap data reporting
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: USI
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: CFTC Data Management Branch 'Unique Swap Identifier (USI) Data Standard', October 1, 2012, usidatastandards100112.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: unique swap identifier
type: Ontology Class
---

# unique swap identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier>

## Definition

identifier for a swap that is used in recordkeeping and swap data reporting

## Relationships

- **Subclass of**: [FinancialInstrumentIdentifier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)

## Annotations

- **label**: unique swap identifier
- **definition**: identifier for a swap that is used in recordkeeping and swap data reporting
- **abbreviation**: USI
- **adaptedFrom**: CFTC Data Management Branch 'Unique Swap Identifier (USI) Data Standard', October 1, 2012, usidatastandards100112.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
