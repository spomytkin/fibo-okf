---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: volatility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical measure of the dispersion around the average of some random variable over some period of time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Dispersion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/Volatility
sources:
- id: fibo-source-9ab287d189
  resource: references/fibo/IND/Indicators/Indicators.rdf
  sha256: 9ab287d18913717a2862bde09cfa2f404bd475a23e07755db731f30ee51be0a6
  title: FIBO source IND/Indicators/Indicators.rdf
title: volatility
type: Ontology Class
---

# volatility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/Volatility>

## Definition

statistical measure of the dispersion around the average of some random variable over some period of time

## Relationships

- **Subclass of**: [Dispersion](/concepts/fibo/FND/Utilities/Analytics/Dispersion.md)

## Constraints

- **[hasDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDatePeriod>)**: some values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [DatedStructuredCollection](/concepts/fibo/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)

## Annotations

- **label**: volatility
- **definition**: statistical measure of the dispersion around the average of some random variable over some period of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
