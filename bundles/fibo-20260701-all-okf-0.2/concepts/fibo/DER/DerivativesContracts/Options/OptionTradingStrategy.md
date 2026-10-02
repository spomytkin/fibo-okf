---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option trading strategy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trading tactic involving more than one option type, strike price, or expiration date on the same underlying asset
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that some trading strategies may be considered financial instruments in their own right, but most strategies
      are not. The critical differentiators include whether the strategy itself can be traded, whether it has a financial
      instrument identifier independently from the identifier(s) of the embedded instrument(s), such as a FIGI or ISIN, and
      so forth.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Option trading strategies refer to buying calls or put options or selling calls or put options or both together
      for the purpose of limiting losses and/or optimizing profits. Basically, these strategies utilize one or more combinations
      for the best outcome possible based on defined parameters. Simple combinations include option spread trades such as
      vertical spreads, calendar (or horizontal) spreads, and diagonal spreads. More involved combinations include trades
      such as condor or butterfly spreads which are actually combinations of two vertical spreads.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradingStrategy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/TradingStrategy
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: option trading strategy
type: Ontology Class
---

# option trading strategy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy>

## Definition

trading tactic involving more than one option type, strike price, or expiration date on the same underlying asset

## Relationships

- **Subclass of**: [TradingStrategy](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/TradingStrategy.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [Option](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Option.md)

## Annotations

- **label** (en): option trading strategy
- **definition** (en): trading tactic involving more than one option type, strike price, or expiration date on the same underlying asset
- **explanatoryNote** (en): Note that some trading strategies may be considered financial instruments in their own right, but most strategies are not. The critical differentiators include whether the strategy itself can be traded, whether it has a financial instrument identifier independently from the identifier(s) of the embedded instrument(s), such as a FIGI or ISIN, and so forth.
- **explanatoryNote** (en): Option trading strategies refer to buying calls or put options or selling calls or put options or both together for the purpose of limiting losses and/or optimizing profits. Basically, these strategies utilize one or more combinations for the best outcome possible based on defined parameters. Simple combinations include option spread trades such as vertical spreads, calendar (or horizontal) spreads, and diagonal spreads. More involved combinations include trades such as condor or butterfly spreads which are actually combinations of two vertical spreads.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
