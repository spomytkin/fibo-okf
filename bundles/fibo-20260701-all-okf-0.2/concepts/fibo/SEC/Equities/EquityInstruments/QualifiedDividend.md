---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: qualified dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dividend that falls under capital gains tax rates that are lower than the income tax rates on unqualified (ordinary)
      dividends
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/QualifiedDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: qualified dividend
type: Ontology Class
---

# qualified dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/QualifiedDividend>

## Definition

dividend that falls under capital gains tax rates that are lower than the income tax rates on unqualified (ordinary) dividends

## Relationships

- **Subclass of**: [Dividend](/concepts/fibo/SEC/Equities/EquityInstruments/Dividend.md)

## Annotations

- **label**: qualified dividend
- **definition**: dividend that falls under capital gains tax rates that are lower than the income tax rates on unqualified (ordinary) dividends

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
