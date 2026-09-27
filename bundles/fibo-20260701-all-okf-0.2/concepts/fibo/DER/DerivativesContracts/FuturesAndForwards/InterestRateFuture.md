---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate future
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: futures contract with an interest-bearing instrument as the underlying asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Most interest rate futures that trade on American exchanges use U.S. Treasury securities, such as Treasury bills,
      Treasury bonds, certificates of deposit, Treasury notes, and Ginnie Mae securities, as the underlying asset.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: N37de0a6bdc2241a1ad1afc4d28099ad1
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/InterestRateFuture
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: interest rate future
type: Ontology Class
---

# interest rate future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/InterestRateFuture>

## Definition

futures contract with an interest-bearing instrument as the underlying asset

## Relationships

- **Subclass of**: [FinancialFuture](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `N37de0a6bdc2241a1ad1afc4d28099ad1`

## Annotations

- **label** (en): interest rate future
- **definition** (en): futures contract with an interest-bearing instrument as the underlying asset
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Most interest rate futures that trade on American exchanges use U.S. Treasury securities, such as Treasury bills, Treasury bonds, certificates of deposit, Treasury notes, and Ginnie Mae securities, as the underlying asset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
