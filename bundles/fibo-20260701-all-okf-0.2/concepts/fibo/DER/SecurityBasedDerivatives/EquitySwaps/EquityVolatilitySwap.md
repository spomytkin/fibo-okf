---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity volatility swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dispersion swap that is a forward contract on the variability of movements in the price of its underlying equities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An equity volatility swap is a measure of the amount by which an asset's price is expected to fluctuate over a
      given period of time; it is normally measured by the annual standard deviation of daily price changes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/DispersionSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionSwap
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityVolatilitySwap
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity volatility swap
type: Ontology Class
---

# equity volatility swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityVolatilitySwap>

## Definition

dispersion swap that is a forward contract on the variability of movements in the price of its underlying equities

## Relationships

- **Subclass of**: [DispersionSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/DispersionSwap.md)
- **Subclass of**: [EquitySwap](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)

## Annotations

- **label** (en): equity volatility swap
- **definition** (en): dispersion swap that is a forward contract on the variability of movements in the price of its underlying equities
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): An equity volatility swap is a measure of the amount by which an asset's price is expected to fluctuate over a given period of time; it is normally measured by the annual standard deviation of daily price changes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
