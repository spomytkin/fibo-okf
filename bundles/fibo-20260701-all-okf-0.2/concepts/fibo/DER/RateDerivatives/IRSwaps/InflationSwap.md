---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inflation swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate swap in which one party pays an amount calculated using an inflation rate index, and the other party pays
      an amount calculated using another inflation rate index, or a fixed or floating interest rate
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InflationLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isLinkedToFallback
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InflationSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: inflation swap
type: Ontology Class
---

# inflation swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InflationSwap>

## Definition

rate swap in which one party pays an amount calculated using an inflation rate index, and the other party pays an amount calculated using another inflation rate index, or a fixed or floating interest rate

## Relationships

- **Subclass of**: [RateBasedDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md)
- **Subclass of**: [RatesSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: some values from of type [InflationLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/InflationLeg.md)
- **[isLinkedToFallback](/concepts/fibo/SEC/Debt/Bonds/isLinkedToFallback.md)**: max qualified cardinality 1 of type [GovernmentBond](/concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md)

## Annotations

- **label** (en): inflation swap
- **definition** (en): rate swap in which one party pays an amount calculated using an inflation rate index, and the other party pays an amount calculated using another inflation rate index, or a fixed or floating interest rate
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
