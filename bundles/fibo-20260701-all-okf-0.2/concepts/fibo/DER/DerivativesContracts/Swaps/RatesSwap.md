---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: rates swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: swap in two counterparties each agree to pay the other cash flows on defined dates during an agreed period, based
      on a specified notional amount and a floating interest, floating inflation or fixed interest rate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RateBasedLeg
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: rates swap
type: Ontology Class
---

# rates swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/RatesSwap>

## Definition

swap in two counterparties each agree to pay the other cash flows on defined dates during an agreed period, based on a specified notional amount and a floating interest, floating inflation or fixed interest rate

## Relationships

- **Subclass of**: [Swap](/concepts/fibo/DER/DerivativesContracts/Swaps/Swap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: exact qualified cardinality 2 of type [RateBasedLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/RateBasedLeg.md)

## Annotations

- **label**: rates swap
- **definition**: swap in two counterparties each agree to pay the other cash flows on defined dates during an agreed period, based on a specified notional amount and a floating interest, floating inflation or fixed interest rate
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
