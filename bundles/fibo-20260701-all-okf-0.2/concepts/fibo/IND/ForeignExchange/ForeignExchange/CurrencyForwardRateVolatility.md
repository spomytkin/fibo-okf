---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency forward rate volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of exchange rate fluctuation based on a range of projected values for exchange rates
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/isVolatilityOf
  subclass_of:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility
  - concept: /concepts/fibo/IND/Indicators/Indicators/ImpliedVolatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/ImpliedVolatility
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRateVolatility
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: currency forward rate volatility
type: Ontology Class
---

# currency forward rate volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRateVolatility>

## Definition

measure of exchange rate fluctuation based on a range of projected values for exchange rates

## Relationships

- **Subclass of**: [ExchangeRateVolatility](/concepts/fibo/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility.md)
- **Subclass of**: [ImpliedVolatility](/concepts/fibo/IND/Indicators/Indicators/ImpliedVolatility.md)

## Constraints

- **[isVolatilityOf](/concepts/fibo/IND/Indicators/Indicators/isVolatilityOf.md)**: all values from of type [CurrencyForwardRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate.md)

## Annotations

- **label**: currency forward rate volatility
- **definition**: measure of exchange rate fluctuation based on a range of projected values for exchange rates

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
