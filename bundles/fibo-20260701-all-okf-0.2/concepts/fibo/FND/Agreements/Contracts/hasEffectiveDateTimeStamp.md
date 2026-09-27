---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has effective date time stamp
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date and time, including time zone, something comes into force
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTimeStamp
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTimeStamp
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDateTimeStamp
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: has effective date time stamp
type: Ontology Property
---

# has effective date time stamp

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDateTimeStamp>

## Definition

indicates the date and time, including time zone, something comes into force

## Relationships

- **Range**: [DateTimeStamp](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTimeStamp>)
- **Subproperty of**: [hasDateTimeStamp](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTimeStamp>)

## Annotations

- **label**: has effective date time stamp
- **definition**: indicates the date and time, including time zone, something comes into force

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
