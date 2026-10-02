---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has reporting period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the reporting period for which a report or something else, such as a market rate or economic indicator,
      applies
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasReportingPeriod
sources:
- id: fibo-source-2c96776dff
  resource: references/fibo/FND/Arrangements/Documents.rdf
  sha256: 2c96776dff29d1955d3d578e07bfed955f6c287acc775b1159190f62e9d82ef3
  title: FIBO source FND/Arrangements/Documents.rdf
title: has reporting period
type: Ontology Property
---

# has reporting period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasReportingPeriod>

## Definition

specifies the reporting period for which a report or something else, such as a market rate or economic indicator, applies

## Relationships

- **Range**: [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label**: has reporting period
- **definition**: specifies the reporting period for which a report or something else, such as a market rate or economic indicator, applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
