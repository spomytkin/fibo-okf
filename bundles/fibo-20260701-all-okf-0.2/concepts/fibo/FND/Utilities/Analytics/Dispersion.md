---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dispersion
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: degree of scatter or variability shown by observations
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Common examples of measures of statistical dispersion are the variance, standard deviation, and interquartile range.
      The collection size argument, above, represents the number of elements in the set, if known. The collection of values
      under consideration is represented as a structured collection in FIBO, typically a sample set derived from a finite
      population.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=3637
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A measure of statistical dispersion is a nonnegative real number that is zero if all the data are the same and
      increases as the data become more diverse.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It is usually measured as an average deviation about some central value (e.g. mean deviation, standard deviation)
      or by an order statistic (e.g. quartile deviation, range) but may also be a mean of deviations of values among themselves
      (e.g. Gini's mean difference and also standard deviation).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/hasCollectionSize
  - filler: https://www.omg.org/spec/Commons/Collections/StructuredCollection
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasObservedValue
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/FinitePopulation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: dispersion
type: Ontology Class
---

# dispersion

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion>

## Definition

degree of scatter or variability shown by observations

## Relationships

- **Subclass of**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasCollectionSize](/concepts/fibo/FND/Arrangements/Arrangements/hasCollectionSize.md)**: max qualified cardinality 1 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[hasObservedValue](/concepts/fibo/FND/Utilities/Analytics/hasObservedValue.md)**: some values from of type [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [FinitePopulation](/concepts/fibo/FND/Utilities/Analytics/FinitePopulation.md)

## Annotations

- **label**: dispersion
- **definition**: degree of scatter or variability shown by observations
- **example**: Common examples of measures of statistical dispersion are the variance, standard deviation, and interquartile range. The collection size argument, above, represents the number of elements in the set, if known. The collection of values under consideration is represented as a structured collection in FIBO, typically a sample set derived from a finite population.
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=3637
- **explanatoryNote**: A measure of statistical dispersion is a nonnegative real number that is zero if all the data are the same and increases as the data become more diverse.
- **explanatoryNote**: It is usually measured as an average deviation about some central value (e.g. mean deviation, standard deviation) or by an order statistic (e.g. quartile deviation, range) but may also be a mean of deviations of values among themselves (e.g. Gini's mean difference and also standard deviation).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
