---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency future
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: futures contract whose underlying asset is an agreement to exchange a specified amount of one currency for another
      at some point in the future based on pricing stated in the contract
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: foreign exchange future
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: forex future
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/CurrencyFuture
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: currency future
type: Ontology Class
---

# currency future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/CurrencyFuture>

## Definition

futures contract whose underlying asset is an agreement to exchange a specified amount of one currency for another at some point in the future based on pricing stated in the contract

## Relationships

- **Subclass of**: [CurrencyDerivative](/concepts/fibo/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- **Subclass of**: [FinancialFuture](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)

## Annotations

- **label** (en): currency future
- **definition** (en): futures contract whose underlying asset is an agreement to exchange a specified amount of one currency for another at some point in the future based on pricing stated in the contract
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **synonym** (en): foreign exchange future
- **synonym** (en): forex future

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
