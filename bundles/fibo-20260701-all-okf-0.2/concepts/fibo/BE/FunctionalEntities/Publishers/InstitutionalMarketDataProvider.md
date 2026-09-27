---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: institutional market data provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: market data provider that supplies multi-asset financial information, analytics, and reference data to financial
      institutions such as banks, asset managers, and trading firms
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Institutional market data providers Offer real-time and historical market data for various asset classes. They
      ensure data accuracy and compliance with regulatory standards. They typically provide tools for data visualization and
      analysis to aid decision-making. They may also facilitate access to proprietary research and market insights. Many such
      firms provide APIs and other options for ease of integration with trading platforms and risk management systems
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/InstitutionalMarketDataProvider
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: institutional market data provider
type: Ontology Class
---

# institutional market data provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/InstitutionalMarketDataProvider>

## Definition

market data provider that supplies multi-asset financial information, analytics, and reference data to financial institutions such as banks, asset managers, and trading firms

## Relationships

- **Subclass of**: [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)

## Annotations

- **label**: institutional market data provider
- **definition**: market data provider that supplies multi-asset financial information, analytics, and reference data to financial institutions such as banks, asset managers, and trading firms
- **explanatoryNote**: Institutional market data providers Offer real-time and historical market data for various asset classes. They ensure data accuracy and compliance with regulatory standards. They typically provide tools for data visualization and analysis to aid decision-making. They may also facilitate access to proprietary research and market insights. Many such firms provide APIs and other options for ease of integration with trading platforms and risk management systems

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
