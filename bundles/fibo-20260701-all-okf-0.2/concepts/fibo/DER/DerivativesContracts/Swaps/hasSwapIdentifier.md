---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has swap identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a swap lifecycle event to the identifier for the swap
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasSwapIdentifier
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: has swap identifier
type: Ontology Property
---

# has swap identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasSwapIdentifier>

## Definition

relates a swap lifecycle event to the identifier for the swap

## Relationships

- **Range**: [FinancialInstrumentIdentifier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label**: has swap identifier
- **definition**: relates a swap lifecycle event to the identifier for the swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
