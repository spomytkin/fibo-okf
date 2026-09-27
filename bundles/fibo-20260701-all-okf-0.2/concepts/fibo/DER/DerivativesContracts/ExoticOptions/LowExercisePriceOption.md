---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: low exercise price option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exotic option that is a European-style call option with an exercise price of one cent that mimics a futures contract
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LEPO
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: LEPOs function as deep-in-the-money options similar to the stock itself. Both buyer and seller of a LEPO operate
      on margin. LEPO options are not available on any U.S. exchanges. Since the strike price is so close to zero, the investor
      purchasing the LEPO gains most of the features of owning the share directly with the major exceptions of dividends and
      voting rights. They are only available with European style expirations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExerciseStyle
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/CallOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LowExercisePriceOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: low exercise price option
type: Ontology Class
---

# low exercise price option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LowExercisePriceOption>

## Definition

exotic option that is a European-style call option with an exercise price of one cent that mimics a futures contract

## Relationships

- **Subclass of**: [CallOption](/concepts/fibo/DER/DerivativesContracts/Options/CallOption.md)
- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasExerciseStyle](/concepts/fibo/DER/DerivativesContracts/Options/hasExerciseStyle.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention`

## Annotations

- **label** (en): low exercise price option
- **definition** (en): exotic option that is a European-style call option with an exercise price of one cent that mimics a futures contract
- **abbreviation** (en): LEPO
- **explanatoryNote** (en): LEPOs function as deep-in-the-money options similar to the stock itself. Both buyer and seller of a LEPO operate on margin. LEPO options are not available on any U.S. exchanges. Since the strike price is so close to zero, the investor purchasing the LEPO gains most of the features of owning the share directly with the major exceptions of dividends and voting rights. They are only available with European style expirations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
