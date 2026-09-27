---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value of a rate established in the marketplace for a set of instruments or that describes the economic climate
      for an industry and/or political region (e.g., SOFR, Prime)
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Financial market rates include, but are not limited to reference rates, foreign exchange rates, lending rates,
      bankers' acceptance rates, and so forth.
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: "Market rates include but may not be limited to the following:\n\t(1) Index: Statistical composite that measures\
      \ changes in the economy or in financial markets, often expressed in percentage changes from a base year or from the\
      \ previous month\n\t(2) Money Rate: Benchmark or guideline for interest rates determined by central banks or economical\
      \ climate as a whole\n\t(3) Bankers' Acceptance Rate: Benchmark reflecting market fluctuations of Bankers' Acceptance\
      \ issued instruments\n\t(4) Commercial Paper Rate: Benchmark reflecting market fluctuations of Commercial Paper issued\
      \ instruments\n\t(5) Certificate of Deposit Rate: Benchmark reflecting market fluctuations of Certificate of Deposit\
      \ issued instruments\n\t(6) Interbank Rate\n\t(7) Prime\n\t(8) Time Deposit Rate: Benchmark reflecting market fluctuations\
      \ of Deposit/Redeposit issued instruments"
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: known collectively (in the CFI Standard) as referential instruments
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/hasQuotationDateTime
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/isValueOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: market rate
type: Ontology Class
---

# market rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate>

## Definition

value of a rate established in the marketplace for a set of instruments or that describes the economic climate for an industry and/or political region (e.g., SOFR, Prime)

## Relationships

- **Subclass of**: [Ratio](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio>)

## Constraints

- **[hasRateValue](/concepts/fibo/FND/Accounting/CurrencyAmount/hasRateValue.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasQuotationDateTime](/concepts/fibo/IND/Indicators/Indicators/hasQuotationDateTime.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[isValueOf](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/isValueOf>)**: min qualified cardinality 0 of type [ScopedMeasure](/concepts/fibo/FND/Utilities/Analytics/ScopedMeasure.md)

## Annotations

- **label**: market rate
- **definition**: value of a rate established in the marketplace for a set of instruments or that describes the economic climate for an industry and/or political region (e.g., SOFR, Prime)
- **example**: Financial market rates include, but are not limited to reference rates, foreign exchange rates, lending rates, bankers' acceptance rates, and so forth.
- **scopeNote**: Market rates include but may not be limited to the following: 	(1) Index: Statistical composite that measures changes in the economy or in financial markets, often expressed in percentage changes from a base year or from the previous month 	(2) Money Rate: Benchmark or guideline for interest rates determined by central banks or economical climate as a whole 	(3) Bankers' Acceptance Rate: Benchmark reflecting market fluctuations of Bankers' Acceptance issued instruments 	(4) Commercial Paper Rate: Benchmark reflecting market fluctuations of Commercial Paper issued instruments 	(5) Certificate of Deposit Rate: Benchmark reflecting market fluctuations of Certificate of Deposit issued instruments 	(6) Interbank Rate 	(7) Prime 	(8) Time Deposit Rate: Benchmark reflecting market fluctuations of Deposit/Redeposit issued instruments
- **scopeNote**: known collectively (in the CFI Standard) as referential instruments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
