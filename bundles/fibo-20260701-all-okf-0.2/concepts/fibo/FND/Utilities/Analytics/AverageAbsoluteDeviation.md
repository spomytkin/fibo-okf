---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: average absolute deviation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: average of the absolute deviations from a central point
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The central point can be the mean, median, mode, or the result of another measure of central tendency. Absolute
      deviation is the distance between each value in the data set and that data set's mean or median.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: mean absolute deviation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
    value: Nc6c8c8c5b65946d1acda682274046435
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Dispersion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/AverageAbsoluteDeviation
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: average absolute deviation
type: Ontology Class
---

# average absolute deviation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/AverageAbsoluteDeviation>

## Definition

average of the absolute deviations from a central point

## Relationships

- **Subclass of**: [Dispersion](/concepts/fibo/FND/Utilities/Analytics/Dispersion.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from value `Nc6c8c8c5b65946d1acda682274046435`

## Annotations

- **label**: average absolute deviation
- **definition**: average of the absolute deviations from a central point
- **explanatoryNote**: The central point can be the mean, median, mode, or the result of another measure of central tendency. Absolute deviation is the distance between each value in the data set and that data set's mean or median.
- **synonym**: mean absolute deviation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
