---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: historical volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of volatility that uses actual values for pricing, rates, and other measurements calculated over some prior
      period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: realized volatility
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/Volatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/Volatility
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/HistoricalVolatility
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: historical volatility
type: Ontology Class
---

# historical volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/HistoricalVolatility>

## Definition

measure of volatility that uses actual values for pricing, rates, and other measurements calculated over some prior period

## Relationships

- **Subclass of**: [Volatility](/concepts/fibo/IND/Indicators/Indicators/Volatility.md)

## Annotations

- **label**: historical volatility
- **definition**: measure of volatility that uses actual values for pricing, rates, and other measurements calculated over some prior period
- **synonym**: realized volatility

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
