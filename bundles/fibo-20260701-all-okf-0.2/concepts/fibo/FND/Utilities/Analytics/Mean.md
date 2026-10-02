---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mean
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: most common measure of central tendency; the average of a set of numbers
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#m
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/glossary/detail.asp?ID=3762
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When unqualified, the mean usually refers to the expectation of a variate, or to the arithmetic mean of a sample
      used as an estimate of the expectation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/symbol
    value: μ
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: expected value
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: first (raw) moment
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
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Mean
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: mean
type: Ontology Class
---

# mean

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Mean>

## Definition

most common measure of central tendency; the average of a set of numbers

## Relationships

- **Subclass of**: [StatisticalMeasure](/concepts/fibo/FND/Utilities/Analytics/StatisticalMeasure.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasObservedValue](/concepts/fibo/FND/Utilities/Analytics/hasObservedValue.md)**: some values from of type [StructuredCollection](<https://www.omg.org/spec/Commons/Collections/StructuredCollection>)

## Annotations

- **label**: mean
- **definition**: most common measure of central tendency; the average of a set of numbers
- **adaptedFrom**: http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#m
- **adaptedFrom**: https://stats.oecd.org/glossary/detail.asp?ID=3762
- **explanatoryNote**: When unqualified, the mean usually refers to the expectation of a variate, or to the arithmetic mean of a sample used as an estimate of the expectation.
- **symbol**: μ
- **synonym**: expected value
- **synonym**: first (raw) moment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
