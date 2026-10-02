---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity variance swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dispersion swap in which the parties agree to exchange payments based on the difference between (i) the realized
      variance of the price changes of a specified equity underlier over a stated observation period and (ii) a fixed amount
      of variance that is agreed when the contract is executed
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An equity variance swap is a forward swap that uses the variance (being the volatility squared) of an underlying's
      price movement over a period as the basis for the payoff calculation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/DispersionSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionSwap
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityVarianceSwap
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity variance swap
type: Ontology Class
---

# equity variance swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityVarianceSwap>

## Definition

dispersion swap in which the parties agree to exchange payments based on the difference between (i) the realized variance of the price changes of a specified equity underlier over a stated observation period and (ii) a fixed amount of variance that is agreed when the contract is executed

## Relationships

- **Subclass of**: [DispersionSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/DispersionSwap.md)
- **Subclass of**: [EquitySwap](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)

## Annotations

- **label** (en): equity variance swap
- **definition** (en): dispersion swap in which the parties agree to exchange payments based on the difference between (i) the realized variance of the price changes of a specified equity underlier over a stated observation period and (ii) a fixed amount of variance that is agreed when the contract is executed
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): An equity variance swap is a forward swap that uses the variance (being the volatility squared) of an underlying's price movement over a period as the basis for the payoff calculation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
