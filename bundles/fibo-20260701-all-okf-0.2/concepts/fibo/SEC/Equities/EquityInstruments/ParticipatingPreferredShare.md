---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: participating preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share that, in addition to paying a stipulated dividend, gives the holder the right to participate with
      common share holders in additional distributions of earnings under specified conditions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Participating preferred shares are rare, typically only issued when needed to attract investors.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/OrdinaryDividend
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividend
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ParticipatingPreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: participating preferred share
type: Ontology Class
---

# participating preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ParticipatingPreferredShare>

## Definition

preferred share that, in addition to paying a stipulated dividend, gives the holder the right to participate with common share holders in additional distributions of earnings under specified conditions

## Relationships

- **Subclass of**: [PreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShare.md)

## Constraints

- **[hasDividend](/concepts/fibo/SEC/Equities/EquityInstruments/hasDividend.md)**: min qualified cardinality 0 of type [OrdinaryDividend](/concepts/fibo/SEC/Equities/EquityInstruments/OrdinaryDividend.md)

## Annotations

- **label**: participating preferred share
- **definition**: preferred share that, in addition to paying a stipulated dividend, gives the holder the right to participate with common share holders in additional distributions of earnings under specified conditions
- **explanatoryNote**: Participating preferred shares are rare, typically only issued when needed to attract investors.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
