---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange-sourced data provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: market data provider that distributes financial information originating directly from trading venues, including
      order-book data, trades, quotes, and venue-specific reference data
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/ExchangeSourcedDataProvider
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: exchange-sourced data provider
type: Ontology Class
---

# exchange-sourced data provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/ExchangeSourcedDataProvider>

## Definition

market data provider that distributes financial information originating directly from trading venues, including order-book data, trades, quotes, and venue-specific reference data

## Relationships

- **Subclass of**: [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)

## Annotations

- **label**: exchange-sourced data provider
- **definition**: market data provider that distributes financial information originating directly from trading venues, including order-book data, trades, quotes, and venue-specific reference data

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
