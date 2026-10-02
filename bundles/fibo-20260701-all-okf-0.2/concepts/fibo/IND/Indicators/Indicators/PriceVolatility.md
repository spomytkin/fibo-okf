---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: price volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical measure of the rate of change in pricing for a given security or market index
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Volatility is modeled here using a structured collection, comprised of a series of individual prices of something
      (a security, index, etc., typically quoted prices), dates, and the source for those prices for some overall period of
      time
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Volatility can be determined using the standard deviation or variance among prices for the security or market index
      over some period of time. For a specific security, volatility may measure the amount and frequency in rapid price fluctuation.
      It is computed as the annualized standard deviation of the percentage change in a security's daily price.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceStructure
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/Volatility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/Volatility
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceVolatility
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: price volatility
type: Ontology Class
---

# price volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceVolatility>

## Definition

statistical measure of the rate of change in pricing for a given security or market index

## Relationships

- **Subclass of**: [Volatility](/concepts/fibo/IND/Indicators/Indicators/Volatility.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [PriceStructure](/concepts/fibo/IND/Indicators/Indicators/PriceStructure.md)

## Annotations

- **label**: price volatility
- **definition**: statistical measure of the rate of change in pricing for a given security or market index
- **editorialNote**: Volatility is modeled here using a structured collection, comprised of a series of individual prices of something (a security, index, etc., typically quoted prices), dates, and the source for those prices for some overall period of time
- **explanatoryNote**: Volatility can be determined using the standard deviation or variance among prices for the security or market index over some period of time. For a specific security, volatility may measure the amount and frequency in rapid price fluctuation. It is computed as the annualized standard deviation of the percentage change in a security's daily price.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
