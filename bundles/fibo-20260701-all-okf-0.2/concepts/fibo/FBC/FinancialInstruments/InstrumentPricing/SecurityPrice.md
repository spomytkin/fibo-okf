---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security price
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: monetary price for a financial instrument at some point in time
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A security price may be the price that some party is willing to pay, has recently paid, or would like to be paid,
      depending on the circumstances.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/isPriceFor
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: security price
type: Ontology Class
---

# security price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice>

## Definition

monetary price for a financial instrument at some point in time

## Relationships

- **Subclass of**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)

## Constraints

- **[hasPricingSource](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasPricingSource.md)**: min qualified cardinality 0
- **[isPriceFor](/concepts/fibo/FND/Accounting/CurrencyAmount/isPriceFor.md)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[hasObservedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/hasObservedDateTime>)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label** (en): security price
- **definition** (en): monetary price for a financial instrument at some point in time
- **explanatoryNote** (en): A security price may be the price that some party is willing to pay, has recently paid, or would like to be paid, depending on the circumstances.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
