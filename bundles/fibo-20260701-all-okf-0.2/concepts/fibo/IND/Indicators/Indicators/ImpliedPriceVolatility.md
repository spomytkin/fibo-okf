---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: implied price volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of volatility that represents the expected fluctuations of an underlying stock or index over a specific
      time frame
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/ImpliedVolatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/ImpliedVolatility
  - concept: /concepts/fibo/IND/Indicators/Indicators/PriceVolatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceVolatility
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/ImpliedPriceVolatility
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: implied price volatility
type: Ontology Class
---

# implied price volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/ImpliedPriceVolatility>

## Definition

measure of volatility that represents the expected fluctuations of an underlying stock or index over a specific time frame

## Relationships

- **Subclass of**: [ImpliedVolatility](/concepts/fibo/IND/Indicators/Indicators/ImpliedVolatility.md)
- **Subclass of**: [PriceVolatility](/concepts/fibo/IND/Indicators/Indicators/PriceVolatility.md)

## Annotations

- **label**: implied price volatility
- **definition**: measure of volatility that represents the expected fluctuations of an underlying stock or index over a specific time frame

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
