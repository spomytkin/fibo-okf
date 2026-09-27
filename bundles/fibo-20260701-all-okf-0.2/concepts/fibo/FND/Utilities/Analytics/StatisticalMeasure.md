---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical measure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: summary (means, mode, total, index, etc.) of the individual quantitative variable values for the statistical units
      in a specific group (study domain)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=5068
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Statistical measures may consist of several orthogonal characteristics, including (a) whether they reflect an estimate
      or variable, (b) the datatype, or from a FIBO perspective, nature of the measure (e.g., index, total, ratio, percent,
      percent change, mean, others), (c) the population (or the universe that applies to the highest level if defined in general)
      to which the measure applies, and (d) any relevant aspects used to subset or stratify a measure, (i.e., make them apply
      to a smaller universe).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/isEstimate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Classifiers/Aspect
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Measure
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: statistical measure
type: Ontology Class
---

# statistical measure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalMeasure>

## Definition

summary (means, mode, total, index, etc.) of the individual quantitative variable values for the statistical units in a specific group (study domain)

## Relationships

- **Subclass of**: [Measure](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Measure>)

## Constraints

- **[isEstimate](/concepts/fibo/FND/Utilities/Analytics/isEstimate.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: min qualified cardinality 0 of type [Aspect](<https://www.omg.org/spec/Commons/Classifiers/Aspect>)

## Annotations

- **label**: statistical measure
- **definition**: summary (means, mode, total, index, etc.) of the individual quantitative variable values for the statistical units in a specific group (study domain)
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=5068
- **explanatoryNote**: Statistical measures may consist of several orthogonal characteristics, including (a) whether they reflect an estimate or variable, (b) the datatype, or from a FIBO perspective, nature of the measure (e.g., index, total, ratio, percent, percent change, mean, others), (c) the population (or the universe that applies to the highest level if defined in general) to which the measure applies, and (d) any relevant aspects used to subset or stratify a measure, (i.e., make them apply to a smaller universe).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
