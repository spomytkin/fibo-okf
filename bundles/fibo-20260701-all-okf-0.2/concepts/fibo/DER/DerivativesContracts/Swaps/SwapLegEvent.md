---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap leg event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap lifecycle event, such as a payment or rate reset event, that applies to one leg of a swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLifecycleEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLifecycleEvent
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLegEvent
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap leg event
type: Ontology Class
---

# swap leg event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLegEvent>

## Definition

swap lifecycle event, such as a payment or rate reset event, that applies to one leg of a swap

## Relationships

- **Subclass of**: [SwapLifecycleEvent](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLifecycleEvent.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)

## Annotations

- **label**: swap leg event
- **definition**: swap lifecycle event, such as a payment or rate reset event, that applies to one leg of a swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
