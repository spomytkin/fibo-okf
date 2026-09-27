---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity price return swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: return swap whose return leg underlier is based on equities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A price return equity swap is similar to a total return swap, except that dividends are not passed through to the
      buyer).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityReturnLeg
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasReturnLeg
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/ReturnSwap
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityPriceReturnSwap
sources:
- id: fibo-source-0de295c2e7
  resource: references/fibo/DER/SecurityBasedDerivatives/EquitySwaps.rdf
  sha256: 0de295c2e7121e0f239ed4c7af84d3182c2c493f2ce6423e02b915331e8a53bb
  title: FIBO source DER/SecurityBasedDerivatives/EquitySwaps.rdf
title: equity price return swap
type: Ontology Class
---

# equity price return swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquityPriceReturnSwap>

## Definition

return swap whose return leg underlier is based on equities

## Relationships

- **Subclass of**: [ReturnSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/ReturnSwap.md)
- **Subclass of**: [EquitySwap](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap.md)

## Constraints

- **[hasReturnLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasReturnLeg.md)**: some values from of type [EquityReturnLeg](/concepts/fibo/DER/SecurityBasedDerivatives/EquitySwaps/EquityReturnLeg.md)

## Annotations

- **label** (en): equity price return swap
- **definition** (en): return swap whose return leg underlier is based on equities
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): A price return equity swap is similar to a total return swap, except that dividends are not passed through to the buyer).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
