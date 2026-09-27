---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap lifecycle event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event that occurs during the lifecycle of a swap, where the overall set of events includes those specific to the
      issuer, front office, middle office, and/or back office processes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasSwapIdentifier
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLifecycleEventIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapParty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleEvent
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLifecycleEvent
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap lifecycle event
type: Ontology Class
---

# swap lifecycle event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLifecycleEvent>

## Definition

event that occurs during the lifecycle of a swap, where the overall set of events includes those specific to the issuer, front office, middle office, and/or back office processes

## Relationships

- **Subclass of**: [LifecycleEvent](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleEvent.md)

## Constraints

- **[hasSwapIdentifier](/concepts/fibo/DER/DerivativesContracts/Swaps/hasSwapIdentifier.md)**: exact qualified cardinality 1 of type [UniqueSwapIdentifier](/concepts/fibo/DER/DerivativesContracts/Swaps/UniqueSwapIdentifier.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: exact qualified cardinality 1 of type [SwapLifecycleEventIdentifier](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLifecycleEventIdentifier.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [SwapParty](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapParty.md)

## Annotations

- **label**: swap lifecycle event
- **definition**: event that occurs during the lifecycle of a swap, where the overall set of events includes those specific to the issuer, front office, middle office, and/or back office processes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
