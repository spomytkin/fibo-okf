---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has request date time
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: date and time at which a request was made
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasRequestDateTime
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: has request date time
type: Ontology Property
---

# has request date time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasRequestDateTime>

## Definition

date and time at which a request was made

## Relationships

- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **Subproperty of**: [hasDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime>)

## Annotations

- **label** (en): has request date time
- **definition** (en): date and time at which a request was made

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
