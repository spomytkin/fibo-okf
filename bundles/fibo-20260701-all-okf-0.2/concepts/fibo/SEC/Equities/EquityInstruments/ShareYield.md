---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: share yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio of the annualized dividend per share divided by the (current) price per share
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: dividend yield
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: dividend-price ratio
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
    value: Ne77c38c1e7c54689a7db879bf00a6867
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/Yield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/Yield
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareYield
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: share yield
type: Ontology Class
---

# share yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareYield>

## Definition

ratio of the annualized dividend per share divided by the (current) price per share

## Relationships

- **Subclass of**: [Yield](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/Yield.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from value `Ne77c38c1e7c54689a7db879bf00a6867`

## Annotations

- **label** (en): share yield
- **definition** (en): ratio of the annualized dividend per share divided by the (current) price per share
- **synonym** (en): dividend yield
- **synonym** (en): dividend-price ratio

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
