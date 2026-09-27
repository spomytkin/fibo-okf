---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity correlation swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: correlation swap that allows one to hedge risks associated with the observed average correlation of a collection
      of underlying equity products
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The underlier for the leg can be any of (1) dividend stream for a single stock, (2) change in value for a single
      share, (3) change in value for a basket of shares, (4) change in value for an index, (5) value of a dividend stream
      for a basket of shares, or (6) comparison of the change in value of a given share or basket or index against something
      else - for example, a single share against an index, which is the thing you are cross-correlating with the volatility
      of the share.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/CorrelationSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/CorrelationSwap
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityCorrelationSwap
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity correlation swap
type: Ontology Class
---

# equity correlation swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityCorrelationSwap>

## Definition

correlation swap that allows one to hedge risks associated with the observed average correlation of a collection of underlying equity products

## Relationships

- **Subclass of**: [CorrelationSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/CorrelationSwap.md)
- **Subclass of**: [EquitySwap](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)

## Annotations

- **label** (en): equity correlation swap
- **definition** (en): correlation swap that allows one to hedge risks associated with the observed average correlation of a collection of underlying equity products
- **explanatoryNote** (en): The underlier for the leg can be any of (1) dividend stream for a single stock, (2) change in value for a single share, (3) change in value for a basket of shares, (4) change in value for an index, (5) value of a dividend stream for a basket of shares, or (6) comparison of the change in value of a given share or basket or index against something else - for example, a single share against an index, which is the thing you are cross-correlating with the volatility of the share.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
