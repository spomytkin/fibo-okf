---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity total return swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: total return swap whose return leg underlier is based on equities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasReturnLeg
    value: Na0c662b1e06444a48f2504bd68f90d82
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/TotalReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/TotalReturnSwap
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityTotalReturnSwap
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity total return swap
type: Ontology Class
---

# equity total return swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityTotalReturnSwap>

## Definition

total return swap whose return leg underlier is based on equities

## Relationships

- **Subclass of**: [TotalReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/TotalReturnSwap.md)
- **Subclass of**: [EquitySwap](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)

## Constraints

- **[hasReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasReturnLeg.md)**: some values from value `Na0c662b1e06444a48f2504bd68f90d82`

## Annotations

- **label** (en): equity total return swap
- **definition** (en): total return swap whose return leg underlier is based on equities
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
