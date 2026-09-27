---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: daily average market rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: overall level of a given rate, calculated as the sum of some selected observed values of the rates for a particular
      reference rate, foreign exchange rate, lending rate, or other market rate divided by the number of samples collected
      over the course of a twenty-four (24) hour period for a specific date
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/m/marketaverage.asp
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/hasQuotationDateTime
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/MarketRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/DailyAverageMarketRate
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: daily average market rate
type: Ontology Class
---

# daily average market rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/DailyAverageMarketRate>

## Definition

overall level of a given rate, calculated as the sum of some selected observed values of the rates for a particular reference rate, foreign exchange rate, lending rate, or other market rate divided by the number of samples collected over the course of a twenty-four (24) hour period for a specific date

## Relationships

- **Subclass of**: [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)

## Constraints

- **[hasQuotationDateTime](/concepts/fibo/IND/Indicators/Indicators/hasQuotationDateTime.md)**: exact qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: daily average market rate
- **definition**: overall level of a given rate, calculated as the sum of some selected observed values of the rates for a particular reference rate, foreign exchange rate, lending rate, or other market rate divided by the number of samples collected over the course of a twenty-four (24) hour period for a specific date
- **adaptedFrom**: http://www.investopedia.com/terms/m/marketaverage.asp

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
