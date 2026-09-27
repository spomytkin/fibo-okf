---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: scoped measure
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: qualified measure that is constrained by filters on the statistical population to which it applies
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that (1) the anchor date reflects the start of the current series, such as 1982-1984 for the CPI, (2) the
      fixed comparative date might be something like March 2009, if one is comparing a current index against its value at
      the end of the great recession, (3) the relative comparative date might be something like a month or year ago, depending
      on the analysis requirements, and (4) the relative comparative period might be a 3 month average prior value, again
      depending on the analysis requirements.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RecurrenceInterval
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/hasPeriodicity
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/FinitePopulation
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalArea
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/QualifiedMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/QualifiedMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: scoped measure
type: Ontology Class
---

# scoped measure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/ScopedMeasure>

## Definition

qualified measure that is constrained by filters on the statistical population to which it applies

## Relationships

- **Subclass of**: [QualifiedMeasure](/concepts/fibo/FND/Utilities/Analytics/QualifiedMeasure.md)

## Constraints

- **[hasPeriodicity](/concepts/fibo/FND/Utilities/Analytics/hasPeriodicity.md)**: all values from of type [RecurrenceInterval](/concepts/fibo/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: min qualified cardinality 0 of type [FinitePopulation](/concepts/fibo/FND/Utilities/Analytics/FinitePopulation.md)
- **[hasCoverageArea](<https://www.omg.org/spec/Commons/Locations/hasCoverageArea>)**: min qualified cardinality 0 of type [StatisticalArea](/concepts/fibo/FND/Utilities/Analytics/StatisticalArea.md)

## Annotations

- **label**: scoped measure
- **definition**: qualified measure that is constrained by filters on the statistical population to which it applies
- **explanatoryNote**: Note that (1) the anchor date reflects the start of the current series, such as 1982-1984 for the CPI, (2) the fixed comparative date might be something like March 2009, if one is comparing a current index against its value at the end of the great recession, (3) the relative comparative date might be something like a month or year ago, depending on the analysis requirements, and (4) the relative comparative period might be a 3 month average prior value, again depending on the analysis requirements.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
