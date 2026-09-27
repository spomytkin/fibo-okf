---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commodity warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: warrant that permits the holder to acquire a specified amount of a commodity during a specified period at a specified
      price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Commodity Warrants Australia (CWA) sells warrants based on 12 commodities and financial markets - crude oil, gold,
      silver, live cattle, corn, orange juice, soy, coffee, cocoa, the Dow Jones Industrial Average, the NASDAQ Composite
      Index and the S&P 500 Index.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
  - concept: /concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/Warrant
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CommodityWarrant
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: commodity warrant
type: Ontology Class
---

# commodity warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/CommodityWarrant>

## Definition

warrant that permits the holder to acquire a specified amount of a commodity during a specified period at a specified price

## Relationships

- **Subclass of**: [CommodityDerivative](/concepts/fibo/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- **Subclass of**: [Warrant](/concepts/fibo/DER/DerivativesContracts/RightsAndWarrants/Warrant.md)

## Annotations

- **label** (en): commodity warrant
- **definition** (en): warrant that permits the holder to acquire a specified amount of a commodity during a specified period at a specified price
- **example** (en): Commodity Warrants Australia (CWA) sells warrants based on 12 commodities and financial markets - crude oil, gold, silver, live cattle, corn, orange juice, soy, coffee, cocoa, the Dow Jones Industrial Average, the NASDAQ Composite Index and the S&P 500 Index.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
