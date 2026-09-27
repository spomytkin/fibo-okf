---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency spot rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rate at which one currency may be exchanged for another for immediate delivery
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Spot rates represent the prices buyers pay in one currency to purchase a second currency. Although the spot exchange
      rate is for delivery on the earliest value date, the standard settlement date for most spot transactions is two business
      days after the transaction date.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotRate
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: currency spot rate
type: Ontology Class
---

# currency spot rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotRate>

## Definition

rate at which one currency may be exchanged for another for immediate delivery

## Relationships

- **Subclass of**: [QuotedExchangeRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)

## Annotations

- **label**: currency spot rate
- **definition**: rate at which one currency may be exchanged for another for immediate delivery
- **explanatoryNote**: Spot rates represent the prices buyers pay in one currency to purchase a second currency. Although the spot exchange rate is for delivery on the earliest value date, the standard settlement date for most spot transactions is two business days after the transaction date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
