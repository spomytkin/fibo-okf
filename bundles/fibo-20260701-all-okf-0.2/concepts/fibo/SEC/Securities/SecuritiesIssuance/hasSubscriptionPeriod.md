---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has subscription period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a period of time in which investors can commit to purchase shares (or units) to be issued
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasSubscriptionPeriod
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: has subscription period
type: Ontology Property
---

# has subscription period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasSubscriptionPeriod>

## Definition

indicates a period of time in which investors can commit to purchase shares (or units) to be issued

## Relationships

- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label**: has subscription period
- **definition**: indicates a period of time in which investors can commit to purchase shares (or units) to be issued

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
