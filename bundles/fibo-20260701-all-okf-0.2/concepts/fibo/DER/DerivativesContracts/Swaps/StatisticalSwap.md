---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap that depends on some statistical measure of the performance of the underlier
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StatisticalSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: statistical swap
type: Ontology Class
---

# statistical swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StatisticalSwap>

## Definition

swap that depends on some statistical measure of the performance of the underlier

## Relationships

- **Subclass of**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: min qualified cardinality 0 of type [FixedLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FixedLeg.md)
- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: some values from of type [PerformanceBasedVariableLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)

## Annotations

- **label**: statistical swap
- **definition**: swap that depends on some statistical measure of the performance of the underlier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
