---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: correlation swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: over-the-counter statistical derivative that allows one to hedge risks associated with the observed average correlation
      of a collection of underlying products
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Each product that can act as the underlier on which the correlation is based has periodically observable prices,
      such as a commodity, exchange rate, interest rate, or stock index. Correlation trading is a strategy in which the investor
      receives exposure to the average correlation of an index.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/StatisticalSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/StatisticalSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/CorrelationSwap
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: correlation swap
type: Ontology Class
---

# correlation swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/CorrelationSwap>

## Definition

over-the-counter statistical derivative that allows one to hedge risks associated with the observed average correlation of a collection of underlying products

## Relationships

- **Subclass of**: [StatisticalSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/StatisticalSwap.md)

## Annotations

- **label** (en): correlation swap
- **definition** (en): over-the-counter statistical derivative that allows one to hedge risks associated with the observed average correlation of a collection of underlying products
- **explanatoryNote**: Each product that can act as the underlier on which the correlation is based has periodically observable prices, such as a commodity, exchange rate, interest rate, or stock index. Correlation trading is a strategy in which the investor receives exposure to the average correlation of an index.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
