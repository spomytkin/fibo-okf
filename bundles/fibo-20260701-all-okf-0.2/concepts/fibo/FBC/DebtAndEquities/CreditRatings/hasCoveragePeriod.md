---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has coverage period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates something (e.g. a credit report or insurance policy) to the specific time period that it covers
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasCoveragePeriod
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: has coverage period
type: Ontology Property
---

# has coverage period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/hasCoveragePeriod>

## Definition

relates something (e.g. a credit report or insurance policy) to the specific time period that it covers

## Relationships

- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label**: has coverage period
- **definition**: relates something (e.g. a credit report or insurance policy) to the specific time period that it covers

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
