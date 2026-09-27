---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collection of security prices
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: collection consisting of a series of prices, each of which has a specific date and time associated with it, for
      some security
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that such a collection is of prices that may be quoted or may be established through analysis, such as an
      average over a number of markets (composite market) or developed via some pricing model (e.g., matrix pricing).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CollectionOfSecurityPrices
sources:
- id: fibo-source-363d300383
  resource: references/fibo/FBC/FinancialInstruments/InstrumentPricing.rdf
  sha256: 363d3003839bfabc03c9cf49c9cb072f37bff4ffe33009879175986c6719cb71
  title: FIBO source FBC/FinancialInstruments/InstrumentPricing.rdf
title: collection of security prices
type: Ontology Class
---

# collection of security prices

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CollectionOfSecurityPrices>

## Definition

collection consisting of a series of prices, each of which has a specific date and time associated with it, for some security

## Relationships

- **Subclass of**: [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Annotations

- **label** (en): collection of security prices
- **definition** (en): collection consisting of a series of prices, each of which has a specific date and time associated with it, for some security
- **explanatoryNote** (en): Note that such a collection is of prices that may be quoted or may be established through analysis, such as an average over a number of markets (composite market) or developed via some pricing model (e.g., matrix pricing).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
