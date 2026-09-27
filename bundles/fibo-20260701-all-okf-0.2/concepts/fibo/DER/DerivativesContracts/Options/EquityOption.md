---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put
      option) the underlying equity assets specified at a pre-determined price (i.e., the strike price, fixed or calculated),
      on or before a specified date (the expiration date)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For an Equity Option, one contract represents 100 shares of stock. Equity options settle in 'American style'.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseStyle
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseConvention
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/VanillaOption
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/EquityOption
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: equity option
type: Ontology Class
---

# equity option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/EquityOption>

## Definition

option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying equity assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)

## Relationships

- **Subclass of**: [VanillaOption](/concepts/fibo/DER/DerivativesContracts/Options/VanillaOption.md)
- **Subclass of**: [EquityDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)

## Constraints

- **[hasExerciseStyle](/concepts/fibo/DER/DerivativesContracts/Options/hasExerciseStyle.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/AmericanExerciseConvention`

## Annotations

- **label** (en): equity option
- **definition** (en): option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying equity assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): For an Equity Option, one contract represents 100 shares of stock. Equity options settle in 'American style'.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
