---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: instrument pool
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pool consisting of financial instruments that may be included in the same investment vehicle
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/Pool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPool
sources:
- id: fibo-source-73259da08c
  resource: references/fibo/SEC/Securities/Pools.rdf
  sha256: 73259da08ce2d3336ab19acd98a9182e1bef062fb636a27936e96545e083ec39
  title: FIBO source SEC/Securities/Pools.rdf
title: instrument pool
type: Ontology Class
---

# instrument pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/InstrumentPool>

## Definition

pool consisting of financial instruments that may be included in the same investment vehicle

## Relationships

- **Subclass of**: [Pool](/concepts/fibo/SEC/Securities/Pools/Pool.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Annotations

- **label**: instrument pool
- **definition**: pool consisting of financial instruments that may be included in the same investment vehicle

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
