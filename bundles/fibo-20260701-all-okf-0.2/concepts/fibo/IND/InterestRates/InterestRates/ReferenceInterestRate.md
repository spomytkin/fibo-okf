---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reference interest rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: market rate that is a rate of interest paid by or agreed among some bank or set of banks
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The reference rate is a moving index such as EURIBOR, the prime rate or the rate on benchmark U.S. Treasuries.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasRateResetTimeOfDay
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasReferenceCurrency
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasTenor
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityKind
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate
  - concept: /concepts/fibo/IND/Indicators/Indicators/MarketRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: reference interest rate
type: Ontology Class
---

# reference interest rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate>

## Definition

market rate that is a rate of interest paid by or agreed among some bank or set of banks

## Relationships

- **Subclass of**: [InterestRate](/concepts/fibo/FND/Accounting/CurrencyAmount/InterestRate.md)
- **Subclass of**: [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)

## Constraints

- **[hasRateResetTimeOfDay](/concepts/fibo/IND/InterestRates/InterestRates/hasRateResetTimeOfDay.md)**: min qualified cardinality 0 of type [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **[hasReferenceCurrency](/concepts/fibo/IND/InterestRates/InterestRates/hasReferenceCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasTenor](/concepts/fibo/IND/InterestRates/InterestRates/hasTenor.md)**: all values from of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)
- **[hasQuantityKind](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityKind>)**: some values from of type [InterestRateBenchmark](/concepts/fibo/IND/InterestRates/InterestRates/InterestRateBenchmark.md)

## Annotations

- **label**: reference interest rate
- **definition**: market rate that is a rate of interest paid by or agreed among some bank or set of banks
- **explanatoryNote**: The reference rate is a moving index such as EURIBOR, the prime rate or the rate on benchmark U.S. Treasuries.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
