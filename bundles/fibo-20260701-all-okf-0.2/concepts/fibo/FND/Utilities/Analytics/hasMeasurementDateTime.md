---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has measurement date time
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date and time that the measurement was taken
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasMeasurementDateTime
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: has measurement date time
type: Ontology Property
---

# has measurement date time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasMeasurementDateTime>

## Definition

indicates the date and time that the measurement was taken

## Relationships

- **Range**: [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: has measurement date time
- **definition**: indicates the date and time that the measurement was taken

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
