---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: average earnings
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of the average wage an hourly or salaried worker makes in a given period of time
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=4360
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Average earnings are typically calculated on an hourly, daily, weekly, or monthly basis. They may be expressed
      as an amount of money or in terms of a percent change with respect to a prior period, depending on the jurisdiction
      and report.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasReferencePeriod
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/AverageEarnings
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: average earnings
type: Ontology Class
---

# average earnings

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/AverageEarnings>

## Definition

measure of the average wage an hourly or salaried worker makes in a given period of time

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasReferencePeriod](/concepts/fibo/FND/Utilities/Analytics/hasReferencePeriod.md)**: exact qualified cardinality 1 of type [ExplicitRecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/ExplicitRecurrenceInterval.md)

## Annotations

- **label**: average earnings
- **definition**: measure of the average wage an hourly or salaried worker makes in a given period of time
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=4360
- **explanatoryNote**: Average earnings are typically calculated on an hourly, daily, weekly, or monthly basis. They may be expressed as an amount of money or in terms of a percent change with respect to a prior period, depending on the jurisdiction and report.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
