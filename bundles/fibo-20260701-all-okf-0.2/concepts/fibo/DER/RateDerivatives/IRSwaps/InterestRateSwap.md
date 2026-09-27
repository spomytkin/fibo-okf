---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap in which the reference (underlier) for at least one leg is an interest rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exchanges
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: interest rate swap
type: Ontology Class
---

# interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap>

## Definition

swap in which the reference (underlier) for at least one leg is an interest rate

## Relationships

- **Subclass of**: [InterestRateDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md)
- **Subclass of**: [RatesSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md)

## Constraints

- **[exchanges](/concepts/fibo/FND/Relations/Relations/exchanges.md)**: exact qualified cardinality 2 of type [InterestRateSwapLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md)

## Annotations

- **label**: interest rate swap
- **definition**: swap in which the reference (underlier) for at least one leg is an interest rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
