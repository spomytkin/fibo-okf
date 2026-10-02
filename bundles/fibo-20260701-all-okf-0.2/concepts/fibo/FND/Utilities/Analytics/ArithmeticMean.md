---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: arithmetic mean
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sum of a collection of numbers divided by the number of numbers in the collection
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: While the arithmetic mean is often used to report central tendencies, it is not a robust statistic, meaning that
      it is greatly influenced by outliers (values that are very much larger or smaller than most of the values). Notably,
      for skewed distributions, such as the distribution of income for which a few people's incomes are substantially greater
      than most people's, the arithmetic mean may not accord with one's notion of 'middle', and robust statistics, such as
      the median, may be a better description of central tendency.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: average
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Mean.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Mean
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: arithmetic mean
type: Ontology Class
---

# arithmetic mean

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ArithmeticMean>

## Definition

sum of a collection of numbers divided by the number of numbers in the collection

## Relationships

- **Subclass of**: [Mean](/concepts/fibo/FND/Utilities/Analytics/Mean.md)

## Annotations

- **label**: arithmetic mean
- **definition**: sum of a collection of numbers divided by the number of numbers in the collection
- **explanatoryNote**: While the arithmetic mean is often used to report central tendencies, it is not a robust statistic, meaning that it is greatly influenced by outliers (values that are very much larger or smaller than most of the values). Notably, for skewed distributions, such as the distribution of income for which a few people's incomes are substantially greater than most people's, the arithmetic mean may not accord with one's notion of 'middle', and robust statistics, such as the median, may be a better description of central tendency.
- **synonym**: average

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
