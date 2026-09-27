---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: canary exercise terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exercise terms that stipulate that an option may only be exercised on predetermined dates until the first step
      is reached, but not after that point
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/uses
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/CanaryExerciseConvention
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/BermudanExerciseTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/CanaryExerciseTerms
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: canary exercise terms
type: Ontology Class
---

# canary exercise terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/CanaryExerciseTerms>

## Definition

exercise terms that stipulate that an option may only be exercised on predetermined dates until the first step is reached, but not after that point

## Relationships

- **Subclass of**: [BermudanExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/BermudanExerciseTerms.md)

## Constraints

- **[uses](<https://www.omg.org/spec/Commons/ContextualDesignators/uses>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/CanaryExerciseConvention`

## Annotations

- **label** (en): canary exercise terms
- **definition** (en): exercise terms that stipulate that an option may only be exercised on predetermined dates until the first step is reached, but not after that point

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
