---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: economic rate-based derivative
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate-based derivative whose underlier is some economic indicator
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nba1d9740829342f09213083ae43f56d5
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/EconomicRateBasedDerivative
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: economic rate-based derivative
type: Ontology Class
---

# economic rate-based derivative

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/EconomicRateBasedDerivative>

## Definition

rate-based derivative whose underlier is some economic indicator

## Relationships

- **Subclass of**: [RateBasedDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nba1d9740829342f09213083ae43f56d5`

## Annotations

- **label**: economic rate-based derivative
- **definition**: rate-based derivative whose underlier is some economic indicator

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
