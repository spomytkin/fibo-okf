---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has base currency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies a unit of currency representing R units of the dealt currency, where R is the exchange rate value, in
      an exchange rate
  characteristics:
  - inverse_functional
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
  rdf_types:
  - http://www.w3.org/2002/07/owl#InverseFunctionalProperty
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasBaseCurrency
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: has base currency
type: Ontology Property
---

# has base currency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasBaseCurrency>

## Definition

specifies a unit of currency representing R units of the dealt currency, where R is the exchange rate value, in an exchange rate

## Relationships

- **Range**: [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **Subproperty of**: [hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)

## Annotations

- **label**: has base currency
- **definition**: specifies a unit of currency representing R units of the dealt currency, where R is the exchange rate value, in an exchange rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
