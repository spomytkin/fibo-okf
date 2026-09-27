---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency spot mid rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicative middle market (mean of spot buying and selling) rate as observed by the reporting source
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/ForeignExchange/ForeignExchange/CurrencySpotRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotMidRate
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: currency spot mid rate
type: Ontology Class
---

# currency spot mid rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotMidRate>

## Definition

indicative middle market (mean of spot buying and selling) rate as observed by the reporting source

## Relationships

- **Subclass of**: [CurrencySpotRate](/concepts/fibo/IND/ForeignExchange/ForeignExchange/CurrencySpotRate.md)

## Annotations

- **label**: currency spot mid rate
- **definition**: indicative middle market (mean of spot buying and selling) rate as observed by the reporting source

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
