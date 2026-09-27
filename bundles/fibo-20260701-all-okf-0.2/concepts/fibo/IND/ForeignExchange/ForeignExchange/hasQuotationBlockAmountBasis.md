---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has quotation block amount basis
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the amount of the dealt currency which would be exchanged in a trade for which the stated spot rate applies
  domain:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuotationBlockAmountBasis
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: has quotation block amount basis
type: Ontology Property
---

# has quotation block amount basis

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuotationBlockAmountBasis>

## Definition

indicates the amount of the dealt currency which would be exchanged in a trade for which the stated spot rate applies

## Relationships

- **Domain**: [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: has quotation block amount basis
- **definition**: indicates the amount of the dealt currency which would be exchanged in a trade for which the stated spot rate applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
