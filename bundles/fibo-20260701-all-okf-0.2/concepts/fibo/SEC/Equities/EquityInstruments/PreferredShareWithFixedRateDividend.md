---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred share with fixed rate dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share whose dividends are set, typically according to the terms of the prospectus
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FixedRateDividend
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: preferred share with fixed rate dividend
type: Ontology Class
---

# preferred share with fixed rate dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend>

## Definition

preferred share whose dividends are set, typically according to the terms of the prospectus

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)

## Constraints

- **[hasDividend](/concepts/fibo/SEC/Equities/EquityInstruments/hasDividend.md)**: min qualified cardinality 0 of type [FixedRateDividend](/concepts/fibo/SEC/Equities/EquityInstruments/FixedRateDividend.md)

## Annotations

- **label**: preferred share with fixed rate dividend
- **definition**: preferred share whose dividends are set, typically according to the terms of the prospectus

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
