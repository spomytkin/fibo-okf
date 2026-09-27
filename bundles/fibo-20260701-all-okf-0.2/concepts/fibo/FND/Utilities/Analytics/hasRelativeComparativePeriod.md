---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has relative comparative period
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a period (typically a prior period) against which the scoped measure is compared, such as an average
      set of values for some period of time compared with a more recent or projected average for a forward looking period
      of time
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasRelativeComparativePeriod
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has relative comparative period
type: Ontology Property
---

# has relative comparative period

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasRelativeComparativePeriod>

## Definition

specifies a period (typically a prior period) against which the scoped measure is compared, such as an average set of values for some period of time compared with a more recent or projected average for a forward looking period of time

## Relationships

- **Range**: [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **Subproperty of**: [hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)

## Annotations

- **label**: has relative comparative period
- **definition**: specifies a period (typically a prior period) against which the scoped measure is compared, such as an average set of values for some period of time compared with a more recent or projected average for a forward looking period of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
