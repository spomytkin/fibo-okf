---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: urban consumer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an economic indicator representing a measure of the average change over time in the prices paid by urban consumers
      for a market basket of consumer goods and services
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CPI-U
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.bls.gov/cpi/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/AmericanStatisticsPublisher
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/isPublishedBy
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Basket
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumerPriceIndex
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: urban consumer price index
type: Ontology Class
---

# urban consumer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumerPriceIndex>

## Definition

an economic indicator representing a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services

## Relationships

- **Subclass of**: [ConsumerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: some values from of type [AmericanStatisticsPublisher](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/AmericanStatisticsPublisher.md)
- **[isPublishedBy](/concepts/fibo/BE/FunctionalEntities/Publishers/isPublishedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [UrbanConsumersUniverse](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: exact qualified cardinality 1 of type [UrbanConsumersUniverse](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [Basket](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md)

## Annotations

- **label**: urban consumer price index
- **definition**: an economic indicator representing a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services
- **abbreviation**: CPI-U
- **adaptedFrom**: http://www.bls.gov/cpi/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
