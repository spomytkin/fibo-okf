---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: performance-based variable leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: floating leg of a swap that depends on some statistical measure of the performance of the underlier
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StatisticalSwap
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/isLegOf
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FloatingLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: performance-based variable leg
type: Ontology Class
---

# performance-based variable leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg>

## Definition

floating leg of a swap that depends on some statistical measure of the performance of the underlier

## Relationships

- **Subclass of**: [FloatingLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FloatingLeg.md)

## Constraints

- **[isLegOf](/concepts/fibo/DER/DerivativesContracts/Swaps/isLegOf.md)**: some values from of type [StatisticalSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/StatisticalSwap.md)

## Annotations

- **label**: performance-based variable leg
- **definition**: floating leg of a swap that depends on some statistical measure of the performance of the underlier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
