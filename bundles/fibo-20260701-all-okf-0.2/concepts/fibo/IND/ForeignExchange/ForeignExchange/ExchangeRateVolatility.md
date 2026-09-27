---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange rate volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical measure of the rate of change in the rate at which one currency can be exchanged for another
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Volatility is modeled here using a structured collection, comprised of a series of individual exchange rates (either
      projected or prior quoted rates), dates, and the source for those rates for some overall period of time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/Volatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/Volatility
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility
sources:
- id: fibo-source-b8e28a4f9e
  resource: references/fibo/IND/ForeignExchange/ForeignExchange.rdf
  sha256: b8e28a4f9e7d1652f38f3d40d54cafac7c6289d49873ee83714b241e5c72d239
  title: FIBO source IND/ForeignExchange/ForeignExchange.rdf
title: exchange rate volatility
type: Ontology Class
---

# exchange rate volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility>

## Definition

statistical measure of the rate of change in the rate at which one currency can be exchanged for another

## Relationships

- **Subclass of**: [Volatility](/concepts/fibo/IND/Indicators/Indicators/Volatility.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [ExchangeRateStructure](/concepts/fibo/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure.md)

## Annotations

- **label**: exchange rate volatility
- **definition**: statistical measure of the rate of change in the rate at which one currency can be exchanged for another
- **usageNote**: Volatility is modeled here using a structured collection, comprised of a series of individual exchange rates (either projected or prior quoted rates), dates, and the source for those rates for some overall period of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
