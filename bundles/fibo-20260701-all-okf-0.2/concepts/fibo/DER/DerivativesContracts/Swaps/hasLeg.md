---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has leg
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a swap contract to a leg that is part of that swap
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: has leg
type: Ontology Property
---

# has leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg>

## Definition

relates a swap contract to a leg that is part of that swap

## Relationships

- **Domain**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)
- **Range**: [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)
- **Subproperty of**: [hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)

## Annotations

- **label**: has leg
- **definition**: relates a swap contract to a leg that is part of that swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
