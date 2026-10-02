---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is premium on
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an exchange rate expressed as a premium on the spot rate for the currency pair
  domain:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate
  range:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/isPremiumOn
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: is premium on
type: Ontology Property
---

# is premium on

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/isPremiumOn>

## Definition

an exchange rate expressed as a premium on the spot rate for the currency pair

## Relationships

- **Domain**: [CurrencyForwardRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate.md)
- **Range**: [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)

## Annotations

- **label**: is premium on
- **definition**: an exchange rate expressed as a premium on the spot rate for the currency pair

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
