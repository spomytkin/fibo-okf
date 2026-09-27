---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has quote currency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the quote currency in an exchange rate; R units of this currency represent one unit of the base currency
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasDealtCurrency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasDealtCurrency
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuoteCurrency
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: has quote currency
type: Ontology Property
---

# has quote currency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuoteCurrency>

## Definition

indicates the quote currency in an exchange rate; R units of this currency represent one unit of the base currency

## Relationships

- **Range**: [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **Subproperty of**: [hasDealtCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasDealtCurrency.md)

## Annotations

- **label**: has quote currency
- **definition**: indicates the quote currency in an exchange rate; R units of this currency represent one unit of the base currency

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
