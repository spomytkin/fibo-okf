---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fixed rate dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dividend that provides a specified annual return on the nominal value (and any premium) paid on shares
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In other words, the return is not variable depending on whether or not the company makes a profit. Annual dividends
      are calculated as a percentage of the par value, which is the price of the preferred stock at the time it was issued.
      Most preferred shares have fixed rate dividends.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasFixedDividendRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FixedRateDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: fixed rate dividend
type: Ontology Class
---

# fixed rate dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FixedRateDividend>

## Definition

dividend that provides a specified annual return on the nominal value (and any premium) paid on shares

## Relationships

- **Subclass of**: [PreferredDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md)

## Constraints

- **[hasFixedDividendRate](/concepts/fibo/SEC/Equities/EquityInstruments/hasFixedDividendRate.md)**: some values from of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label**: fixed rate dividend
- **definition**: dividend that provides a specified annual return on the nominal value (and any premium) paid on shares
- **explanatoryNote**: In other words, the return is not variable depending on whether or not the company makes a profit. Annual dividends are calculated as a percentage of the par value, which is the price of the preferred stock at the time it was issued. Most preferred shares have fixed rate dividends.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
