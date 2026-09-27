---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: composite market
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: group of exchanges and trading venues referenced for pricing purposes
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/StructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CompositeMarket
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: composite market
type: Ontology Class
---

# composite market

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CompositeMarket>

## Definition

group of exchanges and trading venues referenced for pricing purposes

## Relationships

- **Subclass of**: [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Annotations

- **label** (en): composite market
- **definition** (en): group of exchanges and trading venues referenced for pricing purposes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
