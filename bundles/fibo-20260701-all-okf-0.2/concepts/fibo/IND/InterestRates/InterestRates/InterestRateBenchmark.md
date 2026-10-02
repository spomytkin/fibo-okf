---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate benchmark
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for regularly updated interest rates that are publicly accessible, typically set by a central bank or
      group of financial institutions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Benchmark rates, such as EURIBOR, the Fed Funds rate, and many others including those identified as FpML rates,
      are used as benchmarks for a variety of debt instruments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isProducedBy
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasRateResetTimeOfDay
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasTenor
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/QuantityKind
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: interest rate benchmark
type: Ontology Class
---

# interest rate benchmark

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark>

## Definition

classifier for regularly updated interest rates that are publicly accessible, typically set by a central bank or group of financial institutions

## Relationships

- **Subclass of**: [QuantityKind](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/QuantityKind>)

## Constraints

- **[isProducedBy](/concepts/fibo/FND/Relations/Relations/isProducedBy.md)**: min qualified cardinality 0 of type [Publisher](/concepts/fibo/BE/FunctionalEntities/Publishers/Publisher.md)
- **[hasRateResetTimeOfDay](/concepts/fibo/IND/InterestRates/InterestRates/hasRateResetTimeOfDay.md)**: min qualified cardinality 0 of type [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **[hasReferenceCurrency](/concepts/fibo/IND/InterestRates/InterestRates/hasReferenceCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasTenor](/concepts/fibo/IND/InterestRates/InterestRates/hasTenor.md)**: min qualified cardinality 0 of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: min qualified cardinality 0 of type [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)

## Annotations

- **label**: interest rate benchmark
- **definition**: classifier for regularly updated interest rates that are publicly accessible, typically set by a central bank or group of financial institutions
- **explanatoryNote**: Benchmark rates, such as EURIBOR, the Fed Funds rate, and many others including those identified as FpML rates, are used as benchmarks for a variety of debt instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
