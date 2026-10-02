---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has exercise style
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the exercise convention specified for the option
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
  range:
  - concept: /concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseConvention.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/ExerciseConvention
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseStyle
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: has exercise style
type: Ontology Property
---

# has exercise style

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseStyle>

## Definition

indicates the exercise convention specified for the option

## Relationships

- **Domain**: [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)
- **Range**: [ExerciseConvention](/concepts/fibo/SEC/Debt/ExerciseConventions/ExerciseConvention.md)
- **Subproperty of**: [isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)

## Annotations

- **label**: has exercise style
- **definition**: indicates the exercise convention specified for the option

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
