---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: population not in the labor force
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the civilian, noninstitutional population, that is considered neither employed nor unemployed by the
      reporting agency during the reporting period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are a number of distinctions with respect to how individuals are counted from country to country, including
      whether or not they are considered employed if they are on unpaid leave for some reason, and whether or not they are
      counted multiple times if they have more than one paying job.
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: population not in the labor force
type: Ontology Class
---

# population not in the labor force

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce>

## Definition

subset of the civilian, noninstitutional population, that is considered neither employed nor unemployed by the reporting agency during the reporting period

## Relationships

- **Subclass of**: [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Constraints

- **Disjoint with**: [CivilianLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)

## Annotations

- **label**: population not in the labor force
- **definition**: subset of the civilian, noninstitutional population, that is considered neither employed nor unemployed by the reporting agency during the reporting period
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
- **explanatoryNote**: There are a number of distinctions with respect to how individuals are counted from country to country, including whether or not they are considered employed if they are on unpaid leave for some reason, and whether or not they are counted multiple times if they have more than one paying job.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
