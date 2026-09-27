---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dispersion swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical derivative used to hedge on the magnitude of a price movement of an underlying asset
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A variance swap is an instrument that allows investors to trade future realized (or historical) volatility against
      current implied volatility.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Some strategies involve selling a variance swap on an index and buying the variance swaps on the individual constituents;
      this particular kind of spread trade is called a variance dispersion trade.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: variance swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionLeg
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/hasLeg
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sk3w.co/documents/volatility_trading.pdf
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/StatisticalSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StatisticalSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: dispersion swap
type: Ontology Class
---

# dispersion swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionSwap>

## Definition

statistical derivative used to hedge on the magnitude of a price movement of an underlying asset

## Relationships

- **See also**: [volatility_trading.pdf](<https://www.sk3w.co/documents/volatility_trading.pdf>)
- **Subclass of**: [StatisticalSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/StatisticalSwap.md)

## Constraints

- **[hasLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/hasLeg.md)**: exact qualified cardinality 1 of type [DispersionLeg](/concepts/fibo/DER/DerivativesContracts/Swaps/DispersionLeg.md)

## Annotations

- **label** (en): dispersion swap
- **definition** (en): statistical derivative used to hedge on the magnitude of a price movement of an underlying asset
- **explanatoryNote**: A variance swap is an instrument that allows investors to trade future realized (or historical) volatility against current implied volatility.
- **explanatoryNote**: Some strategies involve selling a variance swap on an index and buying the variance swaps on the individual constituents; this particular kind of spread trade is called a variance dispersion trade.
- **synonym** (en): variance swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
