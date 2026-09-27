---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: standardized futures listing terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract terms established by a derivatives exchange that apply to any listing of a futures contract on that exchange.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Individual listings will take on these standard terms but they are not contractual terms of the futures contract,
      they are facts about that listing on that exchange.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DesignatedContractMarket
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/StandardizedFuturesListingTerms
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: standardized futures listing terms
type: Ontology Class
---

# standardized futures listing terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/StandardizedFuturesListingTerms>

## Definition

contract terms established by a derivatives exchange that apply to any listing of a futures contract on that exchange.

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- **Subclass of**: [StandardizedTerms](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: some values from of type [DesignatedContractMarket](/concepts/fibo/FBC/FunctionalEntities/Markets/DesignatedContractMarket.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Listing](/concepts/fibo/SEC/Securities/SecuritiesListings/Listing.md)

## Annotations

- **label** (en): standardized futures listing terms
- **definition** (en): contract terms established by a derivatives exchange that apply to any listing of a futures contract on that exchange.
- **explanatoryNote** (en): Individual listings will take on these standard terms but they are not contractual terms of the futures contract, they are facts about that listing on that exchange.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
