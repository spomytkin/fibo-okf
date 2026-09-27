---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: electronic communication network
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: alternative trading system that automatically matches buy and sell orders for securities in the market
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ECN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: ECNs allow brokerages and investors in different geographic areas to trade without a third party involved, offering
      privacy for investors. They also allow after-hours trading, but trading may be subject to commissions and other fees.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.cfainstitute.org/-/media/documents/issue-brief/dark-pools-internalization-and-equity-market-quality-issue-brief
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ElectronicCommunicationNetwork
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: electronic communication network
type: Ontology Class
---

# electronic communication network

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ElectronicCommunicationNetwork>

## Definition

alternative trading system that automatically matches buy and sell orders for securities in the market

## Relationships

- **See also**: [dark-pools-internalization-and-equity-market-quality-issue-brief](<https://www.cfainstitute.org/-/media/documents/issue-brief/dark-pools-internalization-and-equity-market-quality-issue-brief>)
- **Subclass of**: [AlternativeTradingSystem](/concepts/fibo/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md)

## Annotations

- **label**: electronic communication network
- **definition**: alternative trading system that automatically matches buy and sell orders for securities in the market
- **abbreviation**: ECN
- **explanatoryNote**: ECNs allow brokerages and investors in different geographic areas to trade without a third party involved, offering privacy for investors. They also allow after-hours trading, but trading may be subject to commissions and other fees.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
