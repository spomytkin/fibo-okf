---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: derivative instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument that confers on its holders certain rights or obligations, whose value is derived from one
      or more underlying assets
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: The three major categories of derivatives are (1) forward and future contracts, (2) options contracts, and (3)
      swaps. The most common underlying assets include stocks, bonds, commodities, currencies, interest rates and market indexes.
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: Derivatives can be characterized by whether they are exchange-traded or traded over-the-counter (OTC).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 'Parameswaran, Sunil. Fundamentals of Financial Instruments: An Introduction to Stocks, Bonds, Foreign Exchange,
      and Derivatives. John Wiley and Sons (Asia) Pte. Lte., Singapore, 2011.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Derivative contracts owe their availability to the existence of markets for an underlying asset or a portfolio
      of assets on which such agreements are written. The derivative itself is merely a contract between two or more parties.
      Its value is determined by fluctuations in the underlying asset. Most derivatives are characterized by high leverage.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: derivative contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that the quantity value associated with the derivative represents the quantity of the underlier. The price
      of the underlier is included in settlement terms.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CashInstrument.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CashInstrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasSettlementTerms
  - filler: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ValuationTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/hasValuationTerms
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInitialExchangeDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: derivative instrument
type: Ontology Class
---

# derivative instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument>

## Definition

financial instrument that confers on its holders certain rights or obligations, whose value is derived from one or more underlying assets

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **Disjoint with**: [CashInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/CashInstrument.md)
- **[hasSettlementTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/hasSettlementTerms.md)**: some values from of type [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- **[hasValuationTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/hasValuationTerms.md)**: some values from of type [ValuationTerms](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/ValuationTerms.md)
- **[hasInitialExchangeDate](/concepts/fibo/FBC/DebtAndEquities/Debt/hasInitialExchangeDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasUnderlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasUnderlier.md)**: some values from of type [Underlier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Underlier.md)
- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: some values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[hasQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasQuantityValue>)**: min qualified cardinality 0 of type [ScalarQuantityValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/ScalarQuantityValue>)

## Annotations

- **label**: derivative instrument
- **definition**: financial instrument that confers on its holders certain rights or obligations, whose value is derived from one or more underlying assets
- **example**: The three major categories of derivatives are (1) forward and future contracts, (2) options contracts, and (3) swaps. The most common underlying assets include stocks, bonds, commodities, currencies, interest rates and market indexes.
- **scopeNote**: Derivatives can be characterized by whether they are exchange-traded or traded over-the-counter (OTC).
- **adaptedFrom**: Parameswaran, Sunil. Fundamentals of Financial Instruments: An Introduction to Stocks, Bonds, Foreign Exchange, and Derivatives. John Wiley and Sons (Asia) Pte. Lte., Singapore, 2011.
- **explanatoryNote**: Derivative contracts owe their availability to the existence of markets for an underlying asset or a portfolio of assets on which such agreements are written. The derivative itself is merely a contract between two or more parties. Its value is determined by fluctuations in the underlying asset. Most derivatives are characterized by high leverage.
- **synonym**: derivative contract
- **usageNote**: Note that the quantity value associated with the derivative represents the quantity of the underlier. The price of the underlier is included in settlement terms.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
