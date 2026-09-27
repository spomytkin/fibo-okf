---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has buying currency
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the currency purchased with respect to a currency or related instrument
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the buying and selling currencies could be the same under certain circumstances.
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasDealtCurrency.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasDealtCurrency
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasBuyingCurrency
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has buying currency
type: Ontology Property
---

# has buying currency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasBuyingCurrency>

## Definition

indicates the currency purchased with respect to a currency or related instrument

## Relationships

- **Range**: [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **Subproperty of**: [hasDealtCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasDealtCurrency.md)

## Annotations

- **label** (en): has buying currency
- **definition** (en): indicates the currency purchased with respect to a currency or related instrument
- **explanatoryNote** (en): Note that the buying and selling currencies could be the same under certain circumstances.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
