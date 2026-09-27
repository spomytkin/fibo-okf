---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency forward rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate of exchange between two currencies for settlement at some future point in time, expressed as a premium on
      the spot rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/hasSettlementDate
  subclass_of:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: currency forward rate
type: Ontology Class
---

# currency forward rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate>

## Definition

rate of exchange between two currencies for settlement at some future point in time, expressed as a premium on the spot rate

## Relationships

- **Subclass of**: [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)

## Constraints

- **[hasSettlementDate](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/hasSettlementDate.md)**: all values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: currency forward rate
- **definition**: rate of exchange between two currencies for settlement at some future point in time, expressed as a premium on the spot rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
