---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred share with adjustable rate dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share whose dividend rate varies according to some benchmark
  disjoint_with:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AdjustableRateDividend
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithAdjustableRateDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: preferred share with adjustable rate dividend
type: Ontology Class
---

# preferred share with adjustable rate dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithAdjustableRateDividend>

## Definition

preferred share whose dividend rate varies according to some benchmark

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)

## Constraints

- **Disjoint with**: [PreferredShareWithFixedRateDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend.md)
- **[hasDividend](/concepts/fibo/SEC/Equities/EquityInstruments/hasDividend.md)**: min qualified cardinality 0 of type [AdjustableRateDividend](/concepts/fibo/SEC/Equities/EquityInstruments/AdjustableRateDividend.md)

## Annotations

- **label**: preferred share with adjustable rate dividend
- **definition**: preferred share whose dividend rate varies according to some benchmark

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
