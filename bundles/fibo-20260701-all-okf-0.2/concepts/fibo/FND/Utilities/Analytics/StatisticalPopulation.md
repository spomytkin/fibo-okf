---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statistical population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: statistical universe filtered by time and region
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A common aim of statistical analysis is to produce information about some chosen population. In statistical inference,
      a subset of the population (a statistical sample) is chosen to represent the population in a statistical analysis. If
      a sample is chosen properly, characteristics of the entire population that the sample is drawn from can be estimated
      from corresponding characteristics of the sample.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: http://stats.oecd.org/glossary/detail.asp?ID=2079
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPopulationSize
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/FinitePopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/FinitePopulation
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalUniverse
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalPopulation
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: statistical population
type: Ontology Class
---

# statistical population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalPopulation>

## Definition

statistical universe filtered by time and region

## Relationships

- **Related to**: [detail.asp](<http://stats.oecd.org/glossary/detail.asp?ID=2079>)
- **Subclass of**: [FinitePopulation](/concepts/fibo/FND/Utilities/Analytics/FinitePopulation.md)
- **Subclass of**: [StatisticalUniverse](/concepts/fibo/FND/Utilities/Analytics/StatisticalUniverse.md)

## Constraints

- **[hasPopulationSize](/concepts/fibo/FND/Utilities/Analytics/hasPopulationSize.md)**: all values from of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [StatisticalArea](/concepts/fibo/FND/Utilities/Analytics/StatisticalArea.md)
- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: some values from of type [ExplicitDatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDatePeriod>)

## Annotations

- **label**: statistical population
- **definition**: statistical universe filtered by time and region
- **explanatoryNote**: A common aim of statistical analysis is to produce information about some chosen population. In statistical inference, a subset of the population (a statistical sample) is chosen to represent the population in a statistical analysis. If a sample is chosen properly, characteristics of the entire population that the sample is drawn from can be estimated from corresponding characteristics of the sample.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
