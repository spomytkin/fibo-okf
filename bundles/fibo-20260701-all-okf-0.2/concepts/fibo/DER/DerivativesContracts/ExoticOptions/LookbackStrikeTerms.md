---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lookback strike terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms specifying the value of the underlying asset based on analysis during a specific period, typically ending
      in the maturity of the option, whereby the payoff is determined by comparing the strike price with the value of the
      selected price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the case of a fixed strike, the terms depend on whether the option is a call or put. If it is a call, the calculated
      payout reflects the difference between a running maximum value of the observable during the lookback period, and the
      pre-agreed strike.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The payoff may either be the difference between a fixed, pre-agreed Strike Price and the observable, or the difference
      between the best or worst valuable of the observable and the value of that same observable at maturity of the contract
      (these are the Fixed and Floating lookback terms respectively). This (per review at Nordea) is not mutually exclusive
      with the terms for Fixed Strike and Resettable Strike, that is, either of those kinds of strike terms may apply, and
      Lookback strike terms may also apply.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasLookbackPeriod
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceStructure
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/FixedLookbackStrikeExpression
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: lookback strike terms
type: Ontology Class
---

# lookback strike terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms>

## Definition

terms specifying the value of the underlying asset based on analysis during a specific period, typically ending in the maturity of the option, whereby the payoff is determined by comparing the strike price with the value of the selected price

## Relationships

- **Subclass of**: [DerivativeTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)

## Constraints

- **[hasLookbackPeriod](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasLookbackPeriod.md)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [PriceStructure](/concepts/fibo/IND/Indicators/Indicators/PriceStructure.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: min qualified cardinality 0 of type [FixedLookbackStrikeExpression](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/FixedLookbackStrikeExpression.md)
- **[hasExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasExpression>)**: min qualified cardinality 0 of type [FloatingLookbackStrikeExpression](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression.md)

## Annotations

- **label** (en): lookback strike terms
- **definition** (en): terms specifying the value of the underlying asset based on analysis during a specific period, typically ending in the maturity of the option, whereby the payoff is determined by comparing the strike price with the value of the selected price
- **explanatoryNote** (en): In the case of a fixed strike, the terms depend on whether the option is a call or put. If it is a call, the calculated payout reflects the difference between a running maximum value of the observable during the lookback period, and the pre-agreed strike.
- **explanatoryNote** (en): The payoff may either be the difference between a fixed, pre-agreed Strike Price and the observable, or the difference between the best or worst valuable of the observable and the value of that same observable at maturity of the contract (these are the Fixed and Floating lookback terms respectively). This (per review at Nordea) is not mutually exclusive with the terms for Fixed Strike and Resettable Strike, that is, either of those kinds of strike terms may apply, and Lookback strike terms may also apply.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
