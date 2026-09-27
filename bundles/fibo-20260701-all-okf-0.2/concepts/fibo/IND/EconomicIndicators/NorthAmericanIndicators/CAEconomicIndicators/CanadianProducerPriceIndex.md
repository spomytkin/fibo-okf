---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Canadian producer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an economic indicator representing a measure of the change over time in the prices of a fixed-basket of domestic
      producer goods and services
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www23.statcan.gc.ca/imdb-bmdi/pub/indexth-eng.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that Canada does not produce a high level, cross industry PPI per se. Canadian PPIs are published by industry
      sector. Three of the most important are captured in the union defined herein, which may be expanded over time to integrate
      others, as needed.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianStatisticsPublisher
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/isPublishedBy
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/StatisticsCanada
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: N102a34d9e35b49afadfed2711120718a
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianProducerPriceIndex
sources:
- id: fibo-source-a06a0301d8
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
  sha256: a06a0301d8cf8f8081904fa368ef17074ae7806ea3c96fa34eb61634f9bc05d6
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators.rdf
title: Canadian producer price index
type: Ontology Class
---

# Canadian producer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianProducerPriceIndex>

## Definition

an economic indicator representing a measure of the change over time in the prices of a fixed-basket of domestic producer goods and services

## Relationships

- **Subclass of**: [ProducerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/CanadianStatisticsPublisher`
- **[isPublishedBy](/concepts/fibo/BE/FunctionalEntities/Publishers/isPublishedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/CAEconomicIndicators/StatisticsCanada`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from value `N102a34d9e35b49afadfed2711120718a`

## Annotations

- **label**: Canadian producer price index
- **definition**: an economic indicator representing a measure of the change over time in the prices of a fixed-basket of domestic producer goods and services
- **adaptedFrom**: http://www23.statcan.gc.ca/imdb-bmdi/pub/indexth-eng.htm
- **explanatoryNote**: Note that Canada does not produce a high level, cross industry PPI per se. Canadian PPIs are published by industry sector. Three of the most important are captured in the union defined herein, which may be expanded over time to integrate others, as needed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
