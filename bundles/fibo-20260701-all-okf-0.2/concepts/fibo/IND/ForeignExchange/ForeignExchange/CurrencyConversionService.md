---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency conversion service
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: foreign exchange service involving the conversion of currency of one country or group of countries for another,
      typically, but not always, as a counter transaction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A currency exchange service may be provided by a stand-alone business or may be part of the services offered by
      a bank or other financial institution. The currency exchange profits from its services either through adjusting the
      exchange rate or taking a commission.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/ForeignExchangeService.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ForeignExchangeService
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyConversionService
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: currency conversion service
type: Ontology Class
---

# currency conversion service

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyConversionService>

## Definition

foreign exchange service involving the conversion of currency of one country or group of countries for another, typically, but not always, as a counter transaction

## Relationships

- **Subclass of**: [ForeignExchangeService](/concepts/fibo/IND/ForeignExchange/ForeignExchange/ForeignExchangeService.md)

## Annotations

- **label**: currency conversion service
- **definition**: foreign exchange service involving the conversion of currency of one country or group of countries for another, typically, but not always, as a counter transaction
- **explanatoryNote**: A currency exchange service may be provided by a stand-alone business or may be part of the services offered by a bank or other financial institution. The currency exchange profits from its services either through adjusting the exchange rate or taking a commission.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
