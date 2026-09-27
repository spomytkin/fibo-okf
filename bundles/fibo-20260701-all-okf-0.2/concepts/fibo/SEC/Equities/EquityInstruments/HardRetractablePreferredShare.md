---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: hard retractable preferred share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: retractable preferred share whose retraction value must be paid in cash
  disjoint_with:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/SoftRetractablePreferredShare.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SoftRetractablePreferredShare
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/RetractablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RetractablePreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/HardRetractablePreferredShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: hard retractable preferred share
type: Ontology Class
---

# hard retractable preferred share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/HardRetractablePreferredShare>

## Definition

retractable preferred share whose retraction value must be paid in cash

## Relationships

- **Subclass of**: [RetractablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/RetractablePreferredShare.md)

## Constraints

- **Disjoint with**: [SoftRetractablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/SoftRetractablePreferredShare.md)

## Annotations

- **label**: hard retractable preferred share
- **definition**: retractable preferred share whose retraction value must be paid in cash

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
