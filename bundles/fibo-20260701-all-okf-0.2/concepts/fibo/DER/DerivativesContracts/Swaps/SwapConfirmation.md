---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap confirmation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal confirmation that codifies the terms and conditions specific to a lifecycle event with respect to the overall
      transaction between the parties
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapParty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapConfirmation
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/supersedes
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLifecycleEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLifecycleEvent
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapConfirmation
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap confirmation
type: Ontology Class
---

# swap confirmation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapConfirmation>

## Definition

formal confirmation that codifies the terms and conditions specific to a lifecycle event with respect to the overall transaction between the parties

## Relationships

- **Subclass of**: [SwapLifecycleEvent](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLifecycleEvent.md)
- **Subclass of**: [TransactionConfirmation](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: some values from of type [SwapParty](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapParty.md)
- **[supersedes](/concepts/fibo/FND/Agreements/Contracts/supersedes.md)**: all values from of type [SwapConfirmation](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapConfirmation.md)

## Annotations

- **label**: swap confirmation
- **definition**: formal confirmation that codifies the terms and conditions specific to a lifecycle event with respect to the overall transaction between the parties

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
