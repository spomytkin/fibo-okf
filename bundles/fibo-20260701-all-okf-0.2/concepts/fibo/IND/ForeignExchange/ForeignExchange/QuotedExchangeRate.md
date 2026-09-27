---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: quoted exchange rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exchange rate quoted at a specific point in time, for a given block amount of currency as quoted against another
      (base) currency
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An exchange rate of R represents a rate of R units of the quoted currency to 1 unit of the base currency.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasExchangeRateQuotationSource
    value: Nb1361c984ceb43fcad2b5e345a590549
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/hasQuoteCurrency
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
  - concept: /concepts/fibo/IND/Indicators/Indicators/MarketRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: quoted exchange rate
type: Ontology Class
---

# quoted exchange rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate>

## Definition

exchange rate quoted at a specific point in time, for a given block amount of currency as quoted against another (base) currency

## Relationships

- **Subclass of**: [ExchangeRate](/concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md)
- **Subclass of**: [MarketRate](/concepts/fibo/IND/Indicators/Indicators/MarketRate.md)

## Constraints

- **[hasExchangeRateQuotationSource](/concepts/fibo/IND/ForeignExchange/ForeignExchange/hasExchangeRateQuotationSource.md)**: some values from value `Nb1361c984ceb43fcad2b5e345a590549`
- **[hasQuoteCurrency](/concepts/fibo/IND/ForeignExchange/ForeignExchange/hasQuoteCurrency.md)**: exact qualified cardinality 1 of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)

## Annotations

- **label**: quoted exchange rate
- **definition**: exchange rate quoted at a specific point in time, for a given block amount of currency as quoted against another (base) currency
- **explanatoryNote**: An exchange rate of R represents a rate of R units of the quoted currency to 1 unit of the base currency.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
