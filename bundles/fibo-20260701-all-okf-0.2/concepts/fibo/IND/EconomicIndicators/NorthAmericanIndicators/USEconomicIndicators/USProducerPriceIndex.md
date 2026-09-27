---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.S. producer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an economic indicator representing a measure of the change over time in the selling prices received by domestic
      producers for their output
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.bls.gov/ppi/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/AmericanStatisticsPublisher
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/hasPublisher
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/isPublishedBy
    value: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/USProducerPriceIndex
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: U.S. producer price index
type: Ontology Class
---

# U.S. producer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/USProducerPriceIndex>

## Definition

an economic indicator representing a measure of the change over time in the selling prices received by domestic producers for their output

## Relationships

- **Subclass of**: [ProducerPriceIndex](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex.md)

## Constraints

- **[hasPublisher](/concepts/fibo/BE/FunctionalEntities/Publishers/hasPublisher.md)**: some values from of type [AmericanStatisticsPublisher](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/AmericanStatisticsPublisher.md)
- **[isPublishedBy](/concepts/fibo/BE/FunctionalEntities/Publishers/isPublishedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics`

## Annotations

- **label**: U.S. producer price index
- **definition**: an economic indicator representing a measure of the change over time in the selling prices received by domestic producers for their output
- **adaptedFrom**: http://www.bls.gov/ppi/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
