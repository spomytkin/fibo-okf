---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has exercise date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a date on which an option may be exercised as specified in the terms of the contract
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseDate
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: has exercise date
type: Ontology Property
---

# has exercise date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseDate>

## Definition

indicates a date on which an option may be exercised as specified in the terms of the contract

## Relationships

- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label** (en): has exercise date
- **definition** (en): indicates a date on which an option may be exercised as specified in the terms of the contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
