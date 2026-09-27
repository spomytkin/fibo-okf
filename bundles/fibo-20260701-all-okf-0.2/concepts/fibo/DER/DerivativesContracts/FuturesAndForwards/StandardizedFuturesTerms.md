---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: standardized futures terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms established by a derivatives exchange that apply to any futures contract traded on that exchange
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Standard symbology for the commodities are standardized by the exchanges as part of their standard contracts, for
      example trading in standard bushels, commonly defined kinds of oil and so on. These give the units in which lot sizes
      are described and defined.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Future
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/StandardizedFuturesTerms
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: standardized futures terms
type: Ontology Class
---

# standardized futures terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/StandardizedFuturesTerms>

## Definition

contract terms established by a derivatives exchange that apply to any futures contract traded on that exchange

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- **Subclass of**: [StandardizedTerms](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Future](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Future.md)
- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)

## Annotations

- **label** (en): standardized futures terms
- **definition** (en): contract terms established by a derivatives exchange that apply to any futures contract traded on that exchange
- **explanatoryNote** (en): Standard symbology for the commodities are standardized by the exchanges as part of their standard contracts, for example trading in standard bushels, commonly defined kinds of oil and so on. These give the units in which lot sizes are described and defined.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
