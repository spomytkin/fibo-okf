---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: median
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: value of the variate dividing the total frequency of a data sample, population, or probability distribution, into
      two halves
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/glossary/detail.asp?ID=3717
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The basic advantage of the median in describing data compared to the mean is that it is not skewed by extremely
      large or small values, and may provide a better idea of a 'typical' value.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'This measure represents the middle value (if n is odd) or the average of the two middle values (if n is even)
      in an ordered list of data values. The median divides the total frequency distribution into two equal parts: one-half
      of the cases fall below the median and one-half of the cases exceed the median.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/Collections/StructuredCollection
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasObservedValue
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Median
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: median
type: Ontology Class
---

# median

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Median>

## Definition

value of the variate dividing the total frequency of a data sample, population, or probability distribution, into two halves

## Relationships

- **Subclass of**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasObservedValue](/concepts/fibo/FND/Utilities/Analytics/hasObservedValue.md)**: some values from of type [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)

## Annotations

- **label**: median
- **definition**: value of the variate dividing the total frequency of a data sample, population, or probability distribution, into two halves
- **adaptedFrom**: https://stats.oecd.org/glossary/detail.asp?ID=3717
- **explanatoryNote**: The basic advantage of the median in describing data compared to the mean is that it is not skewed by extremely large or small values, and may provide a better idea of a 'typical' value.
- **explanatoryNote**: This measure represents the middle value (if n is odd) or the average of the two middle values (if n is even) in an ordered list of data values. The median divides the total frequency distribution into two equal parts: one-half of the cases fall below the median and one-half of the cases exceed the median.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
