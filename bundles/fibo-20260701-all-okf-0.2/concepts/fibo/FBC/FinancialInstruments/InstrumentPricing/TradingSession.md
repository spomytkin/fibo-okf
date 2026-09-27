---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trading session
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: window of time within a trading day in which orders may be placed and filled
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://financial-dictionary.thefreedictionary.com/Trading+Sessions
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An exchange may have several trading sessions during a day. For example, the exchange may be open from 9 a.m. until
      10:30 a.m., from 11:30 a.m. until 1 p.m., and from 2 p.m. to 3:30 p.m. Holding several trading sessions gives the market
      more time to digest information rationally without having to respond immediately.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasClosingDateTime
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOpeningDateTime
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingSession
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: trading session
type: Ontology Class
---

# trading session

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingSession>

## Definition

window of time within a trading day in which orders may be placed and filled

## Relationships

- **Subclass of**: [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)

## Constraints

- **[hasClosingDateTime](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasClosingDateTime.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasOpeningDateTime](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasOpeningDateTime.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label** (en): trading session
- **definition** (en): window of time within a trading day in which orders may be placed and filled
- **adaptedFrom**: https://financial-dictionary.thefreedictionary.com/Trading+Sessions
- **explanatoryNote** (en): An exchange may have several trading sessions during a day. For example, the exchange may be open from 9 a.m. until 10:30 a.m., from 11:30 a.m. until 1 p.m., and from 2 p.m. to 3:30 p.m. Holding several trading sessions gives the market more time to digest information rationally without having to respond immediately.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
