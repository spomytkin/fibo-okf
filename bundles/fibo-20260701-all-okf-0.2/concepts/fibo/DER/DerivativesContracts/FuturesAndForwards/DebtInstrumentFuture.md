---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt instrument future
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: futures contract whose underlying asset is at least one debt instrument
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N0abd26a5225744a8af584055f6128d62
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: debt instrument future
type: Ontology Class
---

# debt instrument future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture>

## Definition

futures contract whose underlying asset is at least one debt instrument

## Relationships

- **Subclass of**: [FinancialFuture](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)
- **Subclass of**: [DebtInstrumentDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/DebtInstrumentDerivative.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N0abd26a5225744a8af584055f6128d62`

## Annotations

- **label** (en): debt instrument future
- **definition** (en): futures contract whose underlying asset is at least one debt instrument
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
