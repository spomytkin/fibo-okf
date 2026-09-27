---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is senior to
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that a given share (share class) has higher seniority than the related share, meaning that it gives the
      holder a higher claim on the assets of the issuer
  characteristics:
  - transitive
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  range:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/Share.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  - http://www.w3.org/2002/07/owl#TransitiveProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isSeniorTo
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: is senior to
type: Ontology Property
---

# is senior to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/isSeniorTo>

## Definition

indicates that a given share (share class) has higher seniority than the related share, meaning that it gives the holder a higher claim on the assets of the issuer

## Relationships

- **Domain**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)
- **Range**: [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label**: is senior to
- **definition**: indicates that a given share (share class) has higher seniority than the related share, meaning that it gives the holder a higher claim on the assets of the issuer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
