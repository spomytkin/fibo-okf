---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: observed best value
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: observed value of the underlying asset as of some date during the lookback period that is considered the best value
      from the perspective of the option holder during the lookback period (depending on whether the option is a call or put)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasAsOfDate
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/MarketPrice
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ObservedBestValue
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: observed best value
type: Ontology Class
---

# observed best value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/ObservedBestValue>

## Definition

observed value of the underlying asset as of some date during the lookback period that is considered the best value from the perspective of the option holder during the lookback period (depending on whether the option is a call or put)

## Relationships

- **Subclass of**: [MarketPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md)

## Constraints

- **[hasAsOfDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/hasAsOfDate.md)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label** (en): observed best value
- **definition** (en): observed value of the underlying asset as of some date during the lookback period that is considered the best value from the perspective of the option holder during the lookback period (depending on whether the option is a call or put)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
