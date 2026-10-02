---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has floating stock
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of shares that are available for trading, i.e., the number of shares outstanding less closely
      held shares (those held by insiders) and restricted shares
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A relatively small float results in higher volatility, as a large purchase or sell order will have significant
      influence on the value of the stock.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasFloatingStock
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: has floating stock
type: Ontology Property
---

# has floating stock

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasFloatingStock>

## Definition

indicates the number of shares that are available for trading, i.e., the number of shares outstanding less closely held shares (those held by insiders) and restricted shares

## Relationships

- **Range**: [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **Subproperty of**: [hasAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md)

## Annotations

- **label** (en): has floating stock
- **definition** (en): indicates the number of shares that are available for trading, i.e., the number of shares outstanding less closely held shares (those held by insiders) and restricted shares
- **explanatoryNote** (en): A relatively small float results in higher volatility, as a large purchase or sell order will have significant influence on the value of the stock.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
