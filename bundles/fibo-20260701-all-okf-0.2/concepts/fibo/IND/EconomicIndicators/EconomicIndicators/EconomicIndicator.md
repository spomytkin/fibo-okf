---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: economic indicator
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical measure of economic activity that is regular and comparable in the context of a statistical area (region),
      used for analysis of economic performance and predictions of future performance
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Example indicators include the average work week, weekly claims for unemployment insurance, new orders, vendor
      performance, stock prices, and changes in the money supply.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economic Terms, Fifth Edition, 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The two main features of any indicator are the regularity with which they are measured and published, and the fact
      that they are comparable from one release to the next.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasReportingPeriod
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReleaseDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReleaseDateTime
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasSeriesOrigin
  - filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/isSeasonallyAdjusted
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: economic indicator
type: Ontology Class
---

# economic indicator

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator>

## Definition

statistical measure of economic activity that is regular and comparable in the context of a statistical area (region), used for analysis of economic performance and predictions of future performance

## Relationships

- **Subclass of**: [ScopedMeasure](/concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md)

## Constraints

- **[hasReportingPeriod](/concepts/fibo/FND/Arrangements/Documents/hasReportingPeriod.md)**: some values from of type [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)
- **[hasReleaseDate](/concepts/fibo/FND/Utilities/Analytics/hasReleaseDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasReleaseDateTime](/concepts/fibo/FND/Utilities/Analytics/hasReleaseDateTime.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasSeriesOrigin](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasSeriesOrigin.md)**: all values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[isSeasonallyAdjusted](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/isSeasonallyAdjusted.md)**: all values from of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasCoverageArea](<https://www.omg.org/spec/Commons/Locations/hasCoverageArea>)**: some values from of type [GovernmentSpecifiedStatisticalArea](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md)

## Annotations

- **label**: economic indicator
- **definition**: statistical measure of economic activity that is regular and comparable in the context of a statistical area (region), used for analysis of economic performance and predictions of future performance
- **example**: Example indicators include the average work week, weekly claims for unemployment insurance, new orders, vendor performance, stock prices, and changes in the money supply.
- **adaptedFrom**: Barron's Dictionary of Business and Economic Terms, Fifth Edition, 2012
- **explanatoryNote**: The two main features of any indicator are the regularity with which they are measured and published, and the fact that they are comparable from one release to the next.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
