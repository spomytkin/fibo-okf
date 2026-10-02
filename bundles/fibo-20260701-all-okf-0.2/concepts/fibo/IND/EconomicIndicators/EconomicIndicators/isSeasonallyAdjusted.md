---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is seasonally adjusted
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a predicate indicating whether some published formal method is applied that compensates for seasonal variations
      in the population or index value
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Example explanation from the US Bureau of Labor Statistics: Because price data are used for different purposes
      by different groups, the Bureau of Labor Statistics publishes seasonally adjusted as well as unadjusted changes each
      month. ... Seasonal factors used in computing the seasonally adjusted indexes are derived by the X-13ARIMA-SEATS Seasonal
      Adjustment Method. Seasonally adjusted indexes and seasonal factors are computed annually. Each year, the last five
      years of seasonally adjusted data are revised.'
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/isSeasonallyAdjusted
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: is seasonally adjusted
type: Ontology Property
---

# is seasonally adjusted

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/isSeasonallyAdjusted>

## Definition

a predicate indicating whether some published formal method is applied that compensates for seasonal variations in the population or index value

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is seasonally adjusted
- **definition**: a predicate indicating whether some published formal method is applied that compensates for seasonal variations in the population or index value
- **explanatoryNote**: Example explanation from the US Bureau of Labor Statistics: Because price data are used for different purposes by different groups, the Bureau of Labor Statistics publishes seasonally adjusted as well as unadjusted changes each month. ... Seasonal factors used in computing the seasonally adjusted indexes are derived by the X-13ARIMA-SEATS Seasonal Adjustment Method. Seasonally adjusted indexes and seasonal factors are computed annually. Each year, the last five years of seasonally adjusted data are revised.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
