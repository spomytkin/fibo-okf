---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has quotation settlement basis
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the settlement period for a trade for which the stated spot rate applies
  domain:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuotationSettlementBasis
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: has quotation settlement basis
type: Ontology Property
---

# has quotation settlement basis

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuotationSettlementBasis>

## Definition

indicates the settlement period for a trade for which the stated spot rate applies

## Relationships

- **Domain**: [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)
- **Range**: [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label**: has quotation settlement basis
- **definition**: indicates the settlement period for a trade for which the stated spot rate applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
