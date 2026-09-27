---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rate-based leg
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap leg of a rate-based swap based on a floating interest, floating inflation or fixed interest rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/isLegOf
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N48bd294981fb4da283b5e4ae4d006d1b
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RateBasedLeg
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: rate-based leg
type: Ontology Class
---

# rate-based leg

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RateBasedLeg>

## Definition

swap leg of a rate-based swap based on a floating interest, floating inflation or fixed interest rate

## Relationships

- **Subclass of**: [SwapLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/SwapLeg.md)

## Constraints

- **[isLegOf](/concepts/fibo/DER/DerivativesContracts/Swaps/isLegOf.md)**: some values from of type [RatesSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/RatesSwap.md)
- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N48bd294981fb4da283b5e4ae4d006d1b`

## Annotations

- **label** (en): rate-based leg
- **definition** (en): swap leg of a rate-based swap based on a floating interest, floating inflation or fixed interest rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
