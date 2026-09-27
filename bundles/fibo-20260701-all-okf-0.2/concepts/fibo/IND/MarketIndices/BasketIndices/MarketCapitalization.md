---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market capitalization
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: expression representing the perceived value of a company as determined by the stock market at a specific point
      in time
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: market cap
  - language: en
    predicate: https://www.omg.org/spec/Commons/QuantitiesAndUnits/describesActualExpression
    value: number of shares outstanding x price per share
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/hasMarketCapitalizationValue
  - filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharesOutstanding
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareIssuer
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PricePerShare
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/MarketCapitalization
sources:
- id: fibo-source-8b9b76e637
  resource: references/fibo/IND/MarketIndices/BasketIndices.rdf
  sha256: 8b9b76e637aa5b1332f4c7c5c8a862b34e591e273b3a9fd842a28ea66fc5c321
  title: FIBO source IND/MarketIndices/BasketIndices.rdf
title: market capitalization
type: Ontology Class
---

# market capitalization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/MarketCapitalization>

## Definition

expression representing the perceived value of a company as determined by the stock market at a specific point in time

## Relationships

- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasMarketCapitalizationValue](/concepts/fibo/IND/MarketIndices/BasketIndices/hasMarketCapitalizationValue.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasSharesOutstanding](/concepts/fibo/SEC/Equities/EquityInstruments/hasSharesOutstanding.md)**: some values from of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [ShareIssuer](/concepts/fibo/SEC/Equities/EquityInstruments/ShareIssuer.md)
- **[hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)**: some values from of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [PricePerShare](/concepts/fibo/SEC/Equities/EquityInstruments/PricePerShare.md)

## Annotations

- **label** (en): market capitalization
- **definition** (en): expression representing the perceived value of a company as determined by the stock market at a specific point in time
- **synonym** (en): market cap
- **describesActualExpression** (en): number of shares outstanding x price per share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
