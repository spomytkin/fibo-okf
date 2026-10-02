---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: inflation rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing a change in prices of goods and services for a specified period, for a given statistical
      area
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Always either includes or excludes: Energy prices; Food prices. ALL inflation rates cite whether or not they exclude
      energy and food prices. If nothing stated it is assumed they include them.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Inflation rate can be used to define changes, from period-to-period, in wage (wage inflation), house prices or
      producer inputs/outputs. It can be calculated month-over-month and quarter-over-quarter, as well as year-over-year,
      or on any periodic basis required by the publisher and its community of interest.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InflationRate
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: inflation rate
type: Ontology Class
---

# inflation rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InflationRate>

## Definition

economic indicator representing a change in prices of goods and services for a specified period, for a given statistical area

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [GovernmentSpecifiedStatisticalArea](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md)

## Annotations

- **label**: inflation rate
- **definition**: economic indicator representing a change in prices of goods and services for a specified period, for a given statistical area
- **editorialNote**: Always either includes or excludes: Energy prices; Food prices. ALL inflation rates cite whether or not they exclude energy and food prices. If nothing stated it is assumed they include them.
- **explanatoryNote**: Inflation rate can be used to define changes, from period-to-period, in wage (wage inflation), house prices or producer inputs/outputs. It can be calculated month-over-month and quarter-over-quarter, as well as year-over-year, or on any periodic basis required by the publisher and its community of interest.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
