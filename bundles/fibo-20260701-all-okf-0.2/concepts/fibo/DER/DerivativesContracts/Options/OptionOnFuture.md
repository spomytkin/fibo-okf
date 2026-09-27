---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option on future
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option that gives the holder the right, but not the obligation, to buy or sell a specific futures contract at a
      specified price on or before the option's expiration date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
    value: Nce07dd6523d247f3aa99a336138d8769
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseTerms
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionOnFuture
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: option on future
type: Ontology Class
---

# option on future

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionOnFuture>

## Definition

option that gives the holder the right, but not the obligation, to buy or sell a specific futures contract at a specified price on or before the option's expiration date

## Relationships

- **Subclass of**: [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)

## Constraints

- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from value `Nce07dd6523d247f3aa99a336138d8769`
- **[hasExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/hasExerciseTerms.md)**: some values from of type [AmericanExerciseTerms](/concepts/fibo/SEC/Debt/ExerciseConventions/AmericanExerciseTerms.md)

## Annotations

- **label** (en): option on future
- **definition** (en): option that gives the holder the right, but not the obligation, to buy or sell a specific futures contract at a specified price on or before the option's expiration date
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
