---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: butterfly
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: strategy that combines bull and bear spreads with a fixed risk and capped profit
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These spreads are intended as a market-neutral strategy and pay off the most if the underlying asset does not move
      prior to option expiration. They involve either four calls, four puts, or a combination of puts and calls with three
      strike prices. Butterfly spreads pay off the most if the underlying asset price doesn't change before the option expires.
      The upper and lower strike prices are equal distance from the middle, or at-the-money, strike price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 3
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StrikePrice
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/hasExercisePrice
  - cardinality: 4
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Butterfly
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: butterfly
type: Ontology Class
---

# butterfly

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Butterfly>

## Definition

strategy that combines bull and bear spreads with a fixed risk and capped profit

## Relationships

- **Subclass of**: [OptionTradingStrategy](/concepts/fibo/DER/DerivativesContracts/Options/OptionTradingStrategy.md)

## Constraints

- **[hasExercisePrice](/concepts/fibo/DER/DerivativesContracts/Options/hasExercisePrice.md)**: exact qualified cardinality 3 of type [StrikePrice](/concepts/fibo/DER/DerivativesContracts/Options/StrikePrice.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 4 of type [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): butterfly
- **definition** (en): strategy that combines bull and bear spreads with a fixed risk and capped profit
- **explanatoryNote** (en): These spreads are intended as a market-neutral strategy and pay off the most if the underlying asset does not move prior to option expiration. They involve either four calls, four puts, or a combination of puts and calls with three strike prices. Butterfly spreads pay off the most if the underlying asset price doesn't change before the option expires. The upper and lower strike prices are equal distance from the middle, or at-the-money, strike price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
