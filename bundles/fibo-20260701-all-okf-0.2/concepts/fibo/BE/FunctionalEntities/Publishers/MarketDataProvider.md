---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market data provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: publisher that supplies financial information, reference data, analytics, or related datasets used in financial
      markets
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Market data providers include exchanges and independent data vendors, among others. Market valuation and related
      control and risk processes typically require explicit documentation of the source for a given market rate, such as an
      interest rate benchmark, exchange rate, stock prices, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: market data provider
type: Ontology Class
---

# market data provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider>

## Definition

publisher that supplies financial information, reference data, analytics, or related datasets used in financial markets

## Relationships

- **Subclass of**: [Publisher](/concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md)

## Annotations

- **label**: market data provider
- **definition**: publisher that supplies financial information, reference data, analytics, or related datasets used in financial markets
- **explanatoryNote**: Market data providers include exchanges and independent data vendors, among others. Market valuation and related control and risk processes typically require explicit documentation of the source for a given market rate, such as an interest rate benchmark, exchange rate, stock prices, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
