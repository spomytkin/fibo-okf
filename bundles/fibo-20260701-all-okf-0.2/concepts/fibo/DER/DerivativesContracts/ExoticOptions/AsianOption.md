---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Asian option
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: option whose exercise terms involve a payoff determined by the average underlying price (either the strike price
      or the settlement price) of the underlying asset over a predetermined period
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'For an Asian call option using arithmetic averaging and a 30-day period for sampling the data: On Nov. 1, a trader
      purchased a 90-day arithmetic call option on stock XYZ with an exercise price of $22, where the averaging is based on
      the value of the stock after each 30-day period. The stock price after 30, 60, and 90 days was $21.00, $22.00, and $24.00.
      The arithmetic average (mean) is (21.00 + 22.00 + 24.00) / 3 = 22.33. The profit is the average minus the strike price
      22.33 - 22 = 0.33 or $33.00 per 100 share contract. As with standard options, if the average price is below the strike
      price, the loss is limited to the premium paid for the call options.'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: The averaging can be either a geometric or arithmetic average.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, 2019.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These options allow the buyer to purchase (or sell) the underlying asset at the average price instead of the spot
      price. There are various ways to interpret the word 'average,' and that needs to be specified in the options contract.
      Typically, the average price is a geometric or arithmetic average of the price of the underlying asset at discreet intervals,
      which are also specified in the options contract. Because of the averaging feature, Asian options reduce the volatility
      inherent in the option; therefore, Asian options are typically cheaper than European or American options. They are used
      by traders who are exposed to the underlying asset over some time, such as consumers and suppliers of commodities, etc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/hasAsianTailPeriod
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/usesCurrencyInAveraging
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/usesWeightedAverage
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/hasExerciseDate
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOptionClassifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AveragingStrategy
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/ExoticOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOption
sources:
- id: fibo-source-b365451719
  resource: references/fibo/DER/DerivativesContracts/ExoticOptions.rdf
  sha256: b365451719be659b75e34160f67826d1fecf4db25c0e9fcfd80a2aae7ce02aa5
  title: FIBO source DER/DerivativesContracts/ExoticOptions.rdf
title: Asian option
type: Ontology Class
---

# Asian option

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOption>

## Definition

option whose exercise terms involve a payoff determined by the average underlying price (either the strike price or the settlement price) of the underlying asset over a predetermined period

## Relationships

- **Subclass of**: [ExoticOption](/concepts/fibo/DER/DerivativesContracts/Options/ExoticOption.md)

## Constraints

- **[hasAsianTailPeriod](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/hasAsianTailPeriod.md)**: exact qualified cardinality 1 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[usesCurrencyInAveraging](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/usesCurrencyInAveraging.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[usesWeightedAverage](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/usesWeightedAverage.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[hasExerciseDate](/concepts/fibo/SEC/Debt/ExerciseConventions/hasExerciseDate.md)**: exact qualified cardinality 1 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: exact qualified cardinality 1 of type [AsianOptionClassifier](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/AsianOptionClassifier.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: exact qualified cardinality 1 of type [AveragingStrategy](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/AveragingStrategy.md)

## Annotations

- **label** (en): Asian option
- **definition** (en): option whose exercise terms involve a payoff determined by the average underlying price (either the strike price or the settlement price) of the underlying asset over a predetermined period
- **example** (en): For an Asian call option using arithmetic averaging and a 30-day period for sampling the data: On Nov. 1, a trader purchased a 90-day arithmetic call option on stock XYZ with an exercise price of $22, where the averaging is based on the value of the stock after each 30-day period. The stock price after 30, 60, and 90 days was $21.00, $22.00, and $24.00. The arithmetic average (mean) is (21.00 + 22.00 + 24.00) / 3 = 22.33. The profit is the average minus the strike price 22.33 - 22 = 0.33 or $33.00 per 100 share contract. As with standard options, if the average price is below the strike price, the loss is limited to the premium paid for the call options.
- **note** (en): The averaging can be either a geometric or arithmetic average.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, 2019.
- **explanatoryNote** (en): These options allow the buyer to purchase (or sell) the underlying asset at the average price instead of the spot price. There are various ways to interpret the word 'average,' and that needs to be specified in the options contract. Typically, the average price is a geometric or arithmetic average of the price of the underlying asset at discreet intervals, which are also specified in the options contract. Because of the averaging feature, Asian options reduce the volatility inherent in the option; therefore, Asian options are typically cheaper than European or American options. They are used by traders who are exposed to the underlying asset over some time, such as consumers and suppliers of commodities, etc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
