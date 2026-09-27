---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: median absolute deviation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: median of the absolute deviations of observations from the average which may be the arithmetic mean, the median
      or the mode
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Median
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Dispersion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/MedianAbsoluteDeviation
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: median absolute deviation
type: Ontology Class
---

# median absolute deviation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/MedianAbsoluteDeviation>

## Definition

median of the absolute deviations of observations from the average which may be the arithmetic mean, the median or the mode

## Relationships

- **Subclass of**: [Dispersion](/concepts/fibo/FND/Utilities/Analytics/Dispersion.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [Median](/concepts/fibo/FND/Utilities/Analytics/Median.md)

## Annotations

- **label**: median absolute deviation
- **definition**: median of the absolute deviations of observations from the average which may be the arithmetic mean, the median or the mode

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
