---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: weighting function
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: expression or function that determines the relative importance or influence of a given element of a set with respect
      to the whole
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Given a sample size of 1000, and a population of 300M, then the chance that any individual is selected is 1 in
      300K. In that case, 300K is the weight assigned to each of the elements in the sample.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For certain indices, one of the most common weighting factor is by market capitalization. In that case, each of
      the elements in the basket is multiplied by its market cap to determine its relative importance to the basket overall.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With respect to discrete calculations, weighting functions are positive functions defined on discrete sets, such
      as weighted sums and weighted averages.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/WeightingFunction
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: weighting function
type: Ontology Class
---

# weighting function

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/WeightingFunction>

## Definition

expression or function that determines the relative importance or influence of a given element of a set with respect to the whole

## Relationships

- **Subclass of**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Annotations

- **label**: weighting function
- **definition**: expression or function that determines the relative importance or influence of a given element of a set with respect to the whole
- **example**: Given a sample size of 1000, and a population of 300M, then the chance that any individual is selected is 1 in 300K. In that case, 300K is the weight assigned to each of the elements in the sample.
- **explanatoryNote**: For certain indices, one of the most common weighting factor is by market capitalization. In that case, each of the elements in the basket is multiplied by its market cap to determine its relative importance to the basket overall.
- **explanatoryNote**: With respect to discrete calculations, weighting functions are positive functions defined on discrete sets, such as weighted sums and weighted averages.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
