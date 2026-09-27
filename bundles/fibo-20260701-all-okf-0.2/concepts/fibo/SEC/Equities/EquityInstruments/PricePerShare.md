---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: price per share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: price for one share of a given security at some point in time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PPS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: share price
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/isPriceFor
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/UnitPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/UnitPrice
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PricePerShare
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: price per share
type: Ontology Class
---

# price per share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PricePerShare>

## Definition

price for one share of a given security at some point in time

## Relationships

- **Subclass of**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **Subclass of**: [UnitPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/UnitPrice.md)

## Constraints

- **[isPriceFor](/concepts/fibo/FND/Accounting/CurrencyAmount/isPriceFor.md)**: some values from of type [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label**: price per share
- **definition**: price for one share of a given security at some point in time
- **abbreviation**: PPS
- **synonym**: share price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
