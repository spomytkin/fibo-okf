---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: auction rate dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share dividend whose rate is periodically reset through an auction, typically every 7, 14, 28, or 35
      days
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasAdjustableDividendRate
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AuctionRateDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: auction rate dividend
type: Ontology Class
---

# auction rate dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AuctionRateDividend>

## Definition

preferred share dividend whose rate is periodically reset through an auction, typically every 7, 14, 28, or 35 days

## Relationships

- **Subclass of**: [PreferredDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md)

## Constraints

- **[hasAdjustableDividendRate](/concepts/fibo/SEC/Equities/EquityInstruments/hasAdjustableDividendRate.md)**: some values from of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Annotations

- **label**: auction rate dividend
- **definition**: preferred share dividend whose rate is periodically reset through an auction, typically every 7, 14, 28, or 35 days

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
