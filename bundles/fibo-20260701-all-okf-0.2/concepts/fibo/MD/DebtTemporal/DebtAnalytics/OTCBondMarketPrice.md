---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: o t c bond market price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The price determined for the marketplace for a bond which is traded over the counter.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Review comment: Must include Attribution. This is in the model in the form of tha Market Maker (an actor in the
      activity of secondary market trading for OTC-traded debt).'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: o t c bond market price
type: Ontology Class
---

# o t c bond market price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice>

## Definition

The price determined for the marketplace for a bond which is traded over the counter.

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Constraints

- **[hasPricingSource](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource.md)**: some values from of type [DebtSecuritiesMarketMaker](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker.md)

## Annotations

- **label** (en): o t c bond market price
- **definition** (en): The price determined for the marketplace for a bond which is traded over the counter.
- **editorialNote** (en): Review comment: Must include Attribution. This is in the model in the form of tha Market Maker (an actor in the activity of secondary market trading for OTC-traded debt).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
