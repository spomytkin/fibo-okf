---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: American exercise terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exercise terms that stipulate that an option may be exercised on or before the date of expiration
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Under certain circumstances, early exercise may be advantageous to the option holder.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/BermudanExerciseTerms.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseTerms
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/uses
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseConvention
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseTerms
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: American exercise terms
type: Ontology Class
---

# American exercise terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseTerms>

## Definition

exercise terms that stipulate that an option may be exercised on or before the date of expiration

## Relationships

- **Subclass of**: [ExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md)

## Constraints

- **Disjoint with**: [BermudanExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/BermudanExerciseTerms.md)
- **Disjoint with**: [EuropeanExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms.md)
- **[uses](<https://www.omg.org/spec/Commons/ContextualDesignators/uses>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseConvention`

## Annotations

- **label** (en): American exercise terms
- **definition** (en): exercise terms that stipulate that an option may be exercised on or before the date of expiration
- **explanatoryNote** (en): Under certain circumstances, early exercise may be advantageous to the option holder.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
