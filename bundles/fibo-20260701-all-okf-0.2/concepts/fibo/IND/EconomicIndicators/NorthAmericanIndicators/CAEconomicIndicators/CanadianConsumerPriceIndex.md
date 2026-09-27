---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Canadian consumer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing a measure of changes over time in the prices of a fixed basket of consumer goods
      and services that Canadian private households consume
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CPI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/eng/start
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.statcan.gc.ca/en/subjects-start/prices_and_price_indexes/consumer_price_indexes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianStatisticsPublisher
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/isPublishedBy
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/StatisticsCanada
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianHouseholdsConsumersUniverse
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianHouseholdsConsumersUniverse
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/FixedBasket
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianConsumerPriceIndex
sources:
- id: fibo-source-a06a0301d8
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
  sha256: a06a0301d8cf8f8081904fa368ef17074ae7806ea3c96fa34eb61634f9bc05d6
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
title: Canadian consumer price index
type: Ontology Class
---

# Canadian consumer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianConsumerPriceIndex>

## Definition

economic indicator representing a measure of changes over time in the prices of a fixed basket of consumer goods and services that Canadian private households consume

## Relationships

- **Subclass of**: [ConsumerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianStatisticsPublisher`
- **[isPublishedBy](/concepts/fibo/BE/FunctionalEntities/Publishers/isPublishedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/StatisticsCanada`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [CanadianHouseholdsConsumersUniverse](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianHouseholdsConsumersUniverse.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: exact qualified cardinality 1 of type [CanadianHouseholdsConsumersUniverse](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianHouseholdsConsumersUniverse.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [FixedBasket](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md)

## Annotations

- **label**: Canadian consumer price index
- **definition**: economic indicator representing a measure of changes over time in the prices of a fixed basket of consumer goods and services that Canadian private households consume
- **abbreviation**: CPI
- **adaptedFrom**: http://www.statcan.gc.ca/eng/start
- **adaptedFrom**: https://www.statcan.gc.ca/en/subjects-start/prices_and_price_indexes/consumer_price_indexes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
