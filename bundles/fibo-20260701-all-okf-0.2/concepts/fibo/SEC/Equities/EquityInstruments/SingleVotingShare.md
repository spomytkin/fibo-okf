---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: single voting share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share that has the right to exactly one vote
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/confersNumberOfVotesPerShare
    value: '1'
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SingleVotingShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: single voting share
type: Ontology Class
---

# single voting share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SingleVotingShare>

## Definition

share that has the right to exactly one vote

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **[confersNumberOfVotesPerShare](/concepts/fibo/SEC/Equities/EquityInstruments/confersNumberOfVotesPerShare.md)**: has value value `1`

## Annotations

- **label** (en): single voting share
- **definition** (en): share that has the right to exactly one vote

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
