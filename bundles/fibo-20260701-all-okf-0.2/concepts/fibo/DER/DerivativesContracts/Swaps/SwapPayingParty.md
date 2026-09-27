---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap paying party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap party responsible for making payments for a given leg of the transaction as defined in the contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/PayingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/PayingParty
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapParty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapPayingParty
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap paying party
type: Ontology Class
---

# swap paying party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapPayingParty>

## Definition

swap party responsible for making payments for a given leg of the transaction as defined in the contract

## Relationships

- **Subclass of**: [PayingParty](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/PayingParty.md)
- **Subclass of**: [SwapParty](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapParty.md)

## Annotations

- **label**: swap paying party
- **definition**: swap party responsible for making payments for a given leg of the transaction as defined in the contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
