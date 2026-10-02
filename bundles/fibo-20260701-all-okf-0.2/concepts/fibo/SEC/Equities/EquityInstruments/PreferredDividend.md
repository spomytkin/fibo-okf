---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commitment to distribute a portion of earnings to shareholders, similar to a dividend but often with a fixed payment
      amount and schedule
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividendGracePeriod
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasFixedDividendRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: preferred dividend
type: Ontology Class
---

# preferred dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend>

## Definition

commitment to distribute a portion of earnings to shareholders, similar to a dividend but often with a fixed payment amount and schedule

## Relationships

- **Subclass of**: [Dividend](/concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md)

## Constraints

- **[hasDividendGracePeriod](/concepts/fibo/SEC/Equities/EquityInstruments/hasDividendGracePeriod.md)**: max qualified cardinality 1 of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **[hasFixedDividendRate](/concepts/fibo/SEC/Equities/EquityInstruments/hasFixedDividendRate.md)**: max qualified cardinality 1 of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label**: preferred dividend
- **definition**: commitment to distribute a portion of earnings to shareholders, similar to a dividend but often with a fixed payment amount and schedule

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
