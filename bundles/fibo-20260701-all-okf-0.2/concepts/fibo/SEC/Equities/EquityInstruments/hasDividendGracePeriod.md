---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has dividend grace period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a period of time after a dividend payment becomes due, before the issuer is subject to penalties
  domain:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividendGracePeriod
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has dividend grace period
type: Ontology Property
---

# has dividend grace period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasDividendGracePeriod>

## Definition

indicates a period of time after a dividend payment becomes due, before the issuer is subject to penalties

## Relationships

- **Domain**: [PreferredDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md)
- **Range**: [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **Subproperty of**: [hasDuration](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDuration>)

## Annotations

- **label**: has dividend grace period
- **definition**: indicates a period of time after a dividend payment becomes due, before the issuer is subject to penalties

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
