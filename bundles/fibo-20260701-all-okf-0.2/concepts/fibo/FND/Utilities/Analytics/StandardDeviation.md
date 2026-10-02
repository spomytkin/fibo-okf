---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: standard deviation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: square root of variance that measures the spread or dispersion around the mean of a data set
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SD
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#s
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/glossary/detail.asp?ID=3845
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The most widely used measure of dispersion of a frequency distribution introduced by K. Pearson (1893). It is equal
      to the positive square root of the variance. The standard deviation should not be confused with the root mean square
      deviation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: While standard deviation is the most widely-used measure of spread, using squared deviations, it may not be the
      most robust.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/symbol
    value: σ
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
    value: N710c211da2504a03ab459c0ce88a391a
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Dispersion.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Dispersion
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StandardDeviation
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: standard deviation
type: Ontology Class
---

# standard deviation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StandardDeviation>

## Definition

square root of variance that measures the spread or dispersion around the mean of a data set

## Relationships

- **Subclass of**: [Dispersion](/concepts/fibo/FND/Utilities/Analytics/Dispersion.md)

## Constraints

- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from value `N710c211da2504a03ab459c0ce88a391a`

## Annotations

- **label**: standard deviation
- **definition**: square root of variance that measures the spread or dispersion around the mean of a data set
- **abbreviation**: SD
- **adaptedFrom**: http://www.statcan.gc.ca/edu/power-pouvoir/glossary-glossaire/5214842-eng.htm#s
- **adaptedFrom**: https://stats.oecd.org/glossary/detail.asp?ID=3845
- **explanatoryNote**: The most widely used measure of dispersion of a frequency distribution introduced by K. Pearson (1893). It is equal to the positive square root of the variance. The standard deviation should not be confused with the root mean square deviation.
- **explanatoryNote**: While standard deviation is the most widely-used measure of spread, using squared deviations, it may not be the most robust.
- **symbol**: σ

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
