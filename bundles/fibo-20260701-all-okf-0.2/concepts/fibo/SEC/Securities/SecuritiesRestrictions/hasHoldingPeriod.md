---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has holding period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies a holding period applicable to some financial asset
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasHoldingPeriod
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: has holding period
type: Ontology Property
---

# has holding period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasHoldingPeriod>

## Definition

identifies a holding period applicable to some financial asset

## Relationships

- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label**: has holding period
- **definition**: identifies a holding period applicable to some financial asset

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
