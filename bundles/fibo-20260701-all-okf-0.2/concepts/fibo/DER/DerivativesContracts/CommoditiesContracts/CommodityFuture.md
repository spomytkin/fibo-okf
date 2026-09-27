---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity future
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: futures contract to buy or sell a predetermined amount of a commodity at a specific price on a specific date in
      the future
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: CFTC glossary
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019-10
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A commodity future is an agreement to purchase or sell a commodity for delivery in the future: (1) at a price
      that is determined at initiation of the contract; (2) that obligates each party to the contract to fulfill the contract
      at the specified price; (3) that is used to assume or shift price risk; and (4) that may be satisfied by delivery or
      offset.'
  disjoint_with:
  - concept: /concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Future.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Future
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityFuture
sources:
- id: fibo-source-e460829ab0
  resource: references/fibo/DER/DerivativesContracts/CommoditiesContracts.rdf
  sha256: e460829ab039670f9e06a5e2f7c8a0435a5c7529015e0dbe7a9a790464504bd8
  title: FIBO source DER/DerivativesContracts/CommoditiesContracts.rdf
title: commodity future
type: Ontology Class
---

# commodity future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityFuture>

## Definition

futures contract to buy or sell a predetermined amount of a commodity at a specific price on a specific date in the future

## Relationships

- **Subclass of**: [CommodityDerivative](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- **Subclass of**: [Future](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Future.md)

## Constraints

- **Disjoint with**: [FinancialFuture](/concepts/fibo/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)

## Annotations

- **label** (en): commodity future
- **definition** (en): futures contract to buy or sell a predetermined amount of a commodity at a specific price on a specific date in the future
- **adaptedFrom** (en): CFTC glossary
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019-10
- **explanatoryNote** (en): A commodity future is an agreement to purchase or sell a commodity for delivery in the future: (1) at a price that is determined at initiation of the contract; (2) that obligates each party to the contract to fulfill the contract at the specified price; (3) that is used to assume or shift price risk; and (4) that may be satisfied by delivery or offset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
