---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is leg of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates a swap leg to the to the swap that includes it
  domain:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
  inverse_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  range:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/isIncludedIn
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/isLegOf
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: is leg of
type: Ontology Property
---

# is leg of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/isLegOf>

## Definition

relates a swap leg to the to the swap that includes it

## Relationships

- **Domain**: [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)
- **Inverse of**: [hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)
- **Range**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)
- **Subproperty of**: [isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)

## Annotations

- **label**: is leg of
- **definition**: relates a swap leg to the to the swap that includes it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
