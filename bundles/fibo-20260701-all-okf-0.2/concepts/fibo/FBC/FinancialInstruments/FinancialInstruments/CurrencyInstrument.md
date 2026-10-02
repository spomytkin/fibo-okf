---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency instrument
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument used for the purposes of currency trading
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Example currencies include UK pounds, US dollars, Euro. An example currency instrument is spot currency instrument.
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: Each instance of a currency instrument has a one to one relationship with its associated currency.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 'Parameswaran, Sunil. Fundamentals of Financial Instruments: An Introduction to Stocks, Bonds, Foreign Exchange,
      and Derivatives. John Wiley and Sons (Asia) Pte. Lte., Singapore, 2011.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasBuyingCurrency
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasSellingCurrency
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: currency instrument
type: Ontology Class
---

# currency instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument>

## Definition

financial instrument used for the purposes of currency trading

## Relationships

- **Subclass of**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Constraints

- **[hasBuyingCurrency](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasBuyingCurrency.md)**: min qualified cardinality 0 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasSellingCurrency](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasSellingCurrency.md)**: min qualified cardinality 0 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: currency instrument
- **definition**: financial instrument used for the purposes of currency trading
- **example**: Example currencies include UK pounds, US dollars, Euro. An example currency instrument is spot currency instrument.
- **scopeNote**: Each instance of a currency instrument has a one to one relationship with its associated currency.
- **adaptedFrom**: Parameswaran, Sunil. Fundamentals of Financial Instruments: An Introduction to Stocks, Bonds, Foreign Exchange, and Derivatives. John Wiley and Sons (Asia) Pte. Lte., Singapore, 2011.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
