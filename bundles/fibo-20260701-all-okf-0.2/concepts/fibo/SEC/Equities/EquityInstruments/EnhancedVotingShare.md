---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: enhanced voting share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: share that confers more than one vote per share
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/confersNumberOfVotesPerShare
    value: N559897cf669146bdb7bcb82a93b9e6fa
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EnhancedVotingShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: enhanced voting share
type: Ontology Class
---

# enhanced voting share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EnhancedVotingShare>

## Definition

share that confers more than one vote per share

## Relationships

- **Subclass of**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Constraints

- **[confersNumberOfVotesPerShare](/concepts/fibo/SEC/Equities/EquityInstruments/confersNumberOfVotesPerShare.md)**: some values from value `N559897cf669146bdb7bcb82a93b9e6fa`

## Annotations

- **label** (en): enhanced voting share
- **definition** (en): share that confers more than one vote per share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
