---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unemployed population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the civilian labor force that is considered to have had no employment but was available for work, except
      for temporary illness, and had made specific efforts to find employment sometime during a specified period, during the
      reporting period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Persons who were waiting to be recalled to a job from which they had been laid off need not have been looking for
      work to be classified as unemployed.
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasDurationOfUnemployment
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: unemployed population
type: Ontology Class
---

# unemployed population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemployedPopulation>

## Definition

subset of the civilian labor force that is considered to have had no employment but was available for work, except for temporary illness, and had made specific efforts to find employment sometime during a specified period, during the reporting period

## Relationships

- **Subclass of**: [CivilianLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)

## Constraints

- **Disjoint with**: [EmployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md)
- **[hasDurationOfUnemployment](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasDurationOfUnemployment.md)**: some values from of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)

## Annotations

- **label**: unemployed population
- **definition**: subset of the civilian labor force that is considered to have had no employment but was available for work, except for temporary illness, and had made specific efforts to find employment sometime during a specified period, during the reporting period
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
- **explanatoryNote**: Persons who were waiting to be recalled to a job from which they had been laid off need not have been looking for work to be classified as unemployed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
