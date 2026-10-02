---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trading day
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: time span that a particular trading venue is open
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: RTH
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/trading-day
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, and with respect to common stock in particular, trading day means any day on which the stock
      is traded on the principal market, or, if the principal market is not the principal trading market for the common stock,
      then on the principal securities exchange or securities market on which the common stock is then traded, provided that
      'Trading Day' shall not include any day on which the common stock is scheduled to trade on such exchange or market for
      less than 4.5 hours or any day that the common stock is suspended from trading during the final hour of trading on such
      exchange or market (or if such exchange or market does not designate in advance the closing time of trading on such
      exchange or market, then during the hour ending at 4:00:00 p.m., New York time) unless such day is otherwise designated
      as a trading day in writing by the holder.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: regular trading hours
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: By convention it is sufficient to provide a value for hasOpeningDateTime, with hasClosingDateTime being optional.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasClosingDateTime
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasOpeningDateTime
  - kind: has_value
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
    value: https://www.omg.org/spec/Commons/DatesAndTimes/Day
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingDay
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: trading day
type: Ontology Class
---

# trading day

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingDay>

## Definition

time span that a particular trading venue is open

## Relationships

- **Subclass of**: [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)

## Constraints

- **[hasClosingDateTime](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasClosingDateTime.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasOpeningDateTime](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasOpeningDateTime.md)**: exact qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)**: has value value `https://www.omg.org/spec/Commons/DatesAndTimes/Day`

## Annotations

- **label** (en): trading day
- **definition** (en): time span that a particular trading venue is open
- **abbreviation** (en): RTH
- **adaptedFrom**: https://www.lawinsider.com/dictionary/trading-day
- **explanatoryNote** (en): In the United States, and with respect to common stock in particular, trading day means any day on which the stock is traded on the principal market, or, if the principal market is not the principal trading market for the common stock, then on the principal securities exchange or securities market on which the common stock is then traded, provided that 'Trading Day' shall not include any day on which the common stock is scheduled to trade on such exchange or market for less than 4.5 hours or any day that the common stock is suspended from trading during the final hour of trading on such exchange or market (or if such exchange or market does not designate in advance the closing time of trading on such exchange or market, then during the hour ending at 4:00:00 p.m., New York time) unless such day is otherwise designated as a trading day in writing by the holder.
- **synonym** (en): regular trading hours
- **usageNote** (en): By convention it is sufficient to provide a value for hasOpeningDateTime, with hasClosingDateTime being optional.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
