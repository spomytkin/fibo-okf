---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: return swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap in which one leg, the return leg, is based on income generated from some underlier
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedPaymentLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasFundingLeg
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasReturnLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: return swap
type: Ontology Class
---

# return swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap>

## Definition

swap in which one leg, the return leg, is based on income generated from some underlier

## Relationships

- **Subclass of**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)

## Constraints

- **[hasFundingLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasFundingLeg.md)**: some values from of type [FixedPaymentLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/FixedPaymentLeg.md)
- **[hasReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasReturnLeg.md)**: some values from of type [ReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnLeg.md)

## Annotations

- **label** (en): return swap
- **definition** (en): swap in which one leg, the return leg, is based on income generated from some underlier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
