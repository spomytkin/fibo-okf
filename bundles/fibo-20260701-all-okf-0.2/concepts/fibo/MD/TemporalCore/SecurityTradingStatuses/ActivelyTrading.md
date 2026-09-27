---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: actively trading
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Security is actively traded on the exchange or trading facility
  disjoint_with:
  - concept: /concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/TradingHalted.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/TradingHalted
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/ExchangeSecurityTradingStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/ExchangeSecurityTradingStatus
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/ActivelyTrading
sources:
- id: fibo-source-8a03a65ade
  resource: references/fibo/MD/TemporalCore/SecurityTradingStatuses.rdf
  sha256: 8a03a65aded2ec980c264825a2bc807c16de2c9eaf269f974fefbf8780f0ad23
  title: FIBO source MD/TemporalCore/SecurityTradingStatuses.rdf
title: actively trading
type: Ontology Class
---

# actively trading

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/ActivelyTrading>

## Definition

Security is actively traded on the exchange or trading facility

## Relationships

- **Subclass of**: [ExchangeSecurityTradingStatus](/concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/ExchangeSecurityTradingStatus.md)

## Constraints

- **Disjoint with**: [TradingHalted](/concepts/fibo/MD/TemporalCore/SecurityTradingStatuses/TradingHalted.md)

## Annotations

- **label** (en): actively trading
- **definition** (en): Security is actively traded on the exchange or trading facility

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
