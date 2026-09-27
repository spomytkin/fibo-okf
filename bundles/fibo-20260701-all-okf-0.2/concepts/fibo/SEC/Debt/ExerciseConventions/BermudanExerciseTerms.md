---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bermudan exercise terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exercise terms that stipulate that an option may only be exercised on predetermined dates within some exercise
      window, often on one day each month or at the date of expiration
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Bermuda option is named as such because its exercise dates are more flexible than European options and less
      flexible than American options. Thus, it is in the middle, just like Bermuda is between Europe and America. Bermuda
      options are also referred to as Mid-Atlantic, Quasi American, or Semi-American options.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseDate
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseWindow
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/uses
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseConvention
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseTerms
sources:
- id: fibo-source-b0549059cf
  resource: references/fibo/SEC/Debt/ExerciseConventions.rdf
  sha256: b0549059cf085c65a45ceb8097c6a5d1580392da9215ca35ca9afe213b18f5e4
  title: FIBO source SEC/Debt/ExerciseConventions.rdf
title: Bermudan exercise terms
type: Ontology Class
---

# Bermudan exercise terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseTerms>

## Definition

exercise terms that stipulate that an option may only be exercised on predetermined dates within some exercise window, often on one day each month or at the date of expiration

## Relationships

- **Subclass of**: [ExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseTerms.md)

## Constraints

- **Disjoint with**: [EuropeanExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms.md)
- **[hasExerciseDate](/concepts/fibo/SEC/Debt/ExerciseConventions/hasExerciseDate.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasExerciseWindow](/concepts/fibo/SEC/Debt/ExerciseConventions/hasExerciseWindow.md)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[uses](<https://www.omg.org/spec/Commons/ContextualDesignators/uses>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseConvention`

## Annotations

- **label** (en): Bermudan exercise terms
- **definition** (en): exercise terms that stipulate that an option may only be exercised on predetermined dates within some exercise window, often on one day each month or at the date of expiration
- **explanatoryNote** (en): The Bermuda option is named as such because its exercise dates are more flexible than European options and less flexible than American options. Thus, it is in the middle, just like Bermuda is between Europe and America. Bermuda options are also referred to as Mid-Atlantic, Quasi American, or Semi-American options.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
