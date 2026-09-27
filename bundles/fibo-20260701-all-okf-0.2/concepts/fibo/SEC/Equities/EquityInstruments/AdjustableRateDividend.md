---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: adjustable rate dividend
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: dividend that varies with a benchmark
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The value of the dividend from the preferred share is set by a predetermined formula to move with rates, and because
      of this flexibility preferred prices are often more stable then fixed-rate preferred stocks.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasAdjustableDividendRate
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/describesActualExpression
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityKind
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredDividend
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AdjustableRateDividend
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: adjustable rate dividend
type: Ontology Class
---

# adjustable rate dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AdjustableRateDividend>

## Definition

dividend that varies with a benchmark

## Relationships

- **Subclass of**: [PreferredDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredDividend.md)

## Constraints

- **[hasAdjustableDividendRate](/concepts/fibo/SEC/Equities/EquityInstruments/hasAdjustableDividendRate.md)**: some values from of type [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- **[describesActualExpression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/describesActualExpression>)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasQuantityKind](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityKind>)**: min qualified cardinality 0 of type [InterestRateBenchmark](/concepts/fibo/IND/InterestRates/InterestRates/InterestRateBenchmark.md)

## Annotations

- **label**: adjustable rate dividend
- **definition**: dividend that varies with a benchmark
- **explanatoryNote**: The value of the dividend from the preferred share is set by a predetermined formula to move with rates, and because of this flexibility preferred prices are often more stable then fixed-rate preferred stocks.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
