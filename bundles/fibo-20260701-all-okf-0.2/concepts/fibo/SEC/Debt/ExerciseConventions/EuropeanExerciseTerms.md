---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European exercise terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exercise terms that stipulate that an option may only be exercised at the date of expiration
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseDate
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/uses
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: European exercise terms
type: Ontology Class
---

# European exercise terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms>

## Definition

exercise terms that stipulate that an option may only be exercised at the date of expiration

## Relationships

- **Subclass of**: [ExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md)

## Constraints

- **[hasExerciseDate](/concepts/fibo/SEC/Debt/ExerciseConventions/hasExerciseDate.md)**: exact qualified cardinality 1 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[uses](<https://www.omg.org/spec/Commons/ContextualDesignators/uses>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention`

## Annotations

- **label** (en): European exercise terms
- **definition** (en): exercise terms that stipulate that an option may only be exercised at the date of expiration

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
