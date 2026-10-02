---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has rate reset time of day
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the time of day when a change in a benchmark rate is published, typically the same time every business
      day
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasRateResetTimeOfDay
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: has rate reset time of day
type: Ontology Property
---

# has rate reset time of day

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasRateResetTimeOfDay>

## Definition

indicates the time of day when a change in a benchmark rate is published, typically the same time every business day

## Relationships

- **Range**: [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **Subproperty of**: [hasDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateTime>)

## Annotations

- **label**: has rate reset time of day
- **definition**: indicates the time of day when a change in a benchmark rate is published, typically the same time every business day

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
