---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange rate structure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured collection of quoted or projected exchange rates, such that volatility may be constructed for the structure
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: exchange rate structure
type: Ontology Class
---

# exchange rate structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure>

## Definition

structured collection of quoted or projected exchange rates, such that volatility may be constructed for the structure

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [ExchangeRate](/concepts/fibo/FND/Accounting/CurrencyAmount/ExchangeRate.md)

## Annotations

- **label**: exchange rate structure
- **definition**: structured collection of quoted or projected exchange rates, such that volatility may be constructed for the structure

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
