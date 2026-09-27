---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap whose payments are linked to the change in value of underlying equities (e.g. shares, basket of equities or
      index) or their cashflow(s)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Equity swaps can be physically or cash settled.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity swap
type: Ontology Class
---

# equity swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap>

## Definition

swap whose payments are linked to the change in value of underlying equities (e.g. shares, basket of equities or index) or their cashflow(s)

## Relationships

- **Subclass of**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)
- **Subclass of**: [EquityDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)

## Annotations

- **label** (en): equity swap
- **definition** (en): swap whose payments are linked to the change in value of underlying equities (e.g. shares, basket of equities or index) or their cashflow(s)
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): Equity swaps can be physically or cash settled.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
