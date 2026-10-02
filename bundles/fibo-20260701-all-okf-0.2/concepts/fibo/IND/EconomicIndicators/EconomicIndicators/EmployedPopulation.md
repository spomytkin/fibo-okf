---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employed population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the civilian labor force considered to be employed during the reporting period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are a number of distinctions with respect to how individuals are counted from country to country, including
      whether or not they are considered employed if they are on unpaid leave for some reason, and whether or not they are
      counted multiple times if they have more than one paying job.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: employed population
type: Ontology Class
---

# employed population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation>

## Definition

subset of the civilian labor force considered to be employed during the reporting period

## Relationships

- **Subclass of**: [CivilianLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)

## Annotations

- **label**: employed population
- **definition**: subset of the civilian labor force considered to be employed during the reporting period
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
- **explanatoryNote**: There are a number of distinctions with respect to how individuals are counted from country to country, including whether or not they are considered employed if they are on unpaid leave for some reason, and whether or not they are counted multiple times if they have more than one paying job.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
