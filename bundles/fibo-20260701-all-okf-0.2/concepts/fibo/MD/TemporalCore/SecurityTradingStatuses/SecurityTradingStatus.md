---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security trading status
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: status of the security in terms of whether it is trading or not, and any special considerations relating to trading
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Exchange Traded Security trading status is now a separate term, covering trading suspension on an exchange, so
      that does not form part of this term.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/LifecycleStatus
resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus
sources:
- id: fibo-source-8a03a65ade
  resource: references/fibo/MD/TemporalCore/SecurityTradingStatuses.rdf
  sha256: 8a03a65aded2ec980c264825a2bc807c16de2c9eaf269f974fefbf8780f0ad23
  title: FIBO source MD/TemporalCore/SecurityTradingStatuses.rdf
title: security trading status
type: Ontology Class
---

# security trading status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus>

## Definition

status of the security in terms of whether it is trading or not, and any special considerations relating to trading

## Relationships

- **Subclass of**: [LifecycleStatus](/concepts/fibo/FND/Arrangements/Lifecycles/LifecycleStatus.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): security trading status
- **definition** (en): status of the security in terms of whether it is trading or not, and any special considerations relating to trading
- **editorialNote** (en): Exchange Traded Security trading status is now a separate term, covering trading suspension on an exchange, so that does not form part of this term.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
