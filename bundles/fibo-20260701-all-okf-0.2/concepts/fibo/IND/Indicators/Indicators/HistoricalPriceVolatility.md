---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: historical price volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: historical volatility measure of past trading ranges of prices of underlying securities and indexes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Calculations for historical volatility are generally based on the change from one closing price to the next.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/HistoricalVolatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/HistoricalVolatility
  - concept: /concepts/fibo/IND/Indicators/Indicators/PriceVolatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceVolatility
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/HistoricalPriceVolatility
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: historical price volatility
type: Ontology Class
---

# historical price volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/HistoricalPriceVolatility>

## Definition

historical volatility measure of past trading ranges of prices of underlying securities and indexes

## Relationships

- **Subclass of**: [HistoricalVolatility](/concepts/fibo/IND/Indicators/Indicators/HistoricalVolatility.md)
- **Subclass of**: [PriceVolatility](/concepts/fibo/IND/Indicators/Indicators/PriceVolatility.md)

## Annotations

- **label**: historical price volatility
- **definition**: historical volatility measure of past trading ranges of prices of underlying securities and indexes
- **explanatoryNote**: Calculations for historical volatility are generally based on the change from one closing price to the next.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
