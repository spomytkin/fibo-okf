---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employed population part-time for economic reasons
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week due
      to slack work, unfavorable business conditions, inability to find full-time work, and seasonal declines in demand
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/Index.aspx?DatasetCode=STLABOUR
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/cps/definitions.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: involuntary part-time population
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: population employed part-time for economic reasons
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnderemployedPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnderemployedPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForEconomicReasons
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: employed population part-time for economic reasons
type: Ontology Class
---

# employed population part-time for economic reasons

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForEconomicReasons>

## Definition

subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week due to slack work, unfavorable business conditions, inability to find full-time work, and seasonal declines in demand

## Relationships

- **Subclass of**: [EmployedPopulationPartTime](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime.md)
- **Subclass of**: [UnderemployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnderemployedPopulation.md)

## Annotations

- **label**: employed population part-time for economic reasons
- **definition**: subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week due to slack work, unfavorable business conditions, inability to find full-time work, and seasonal declines in demand
- **adaptedFrom**: https://stats.oecd.org/Index.aspx?DatasetCode=STLABOUR
- **adaptedFrom**: https://www.bls.gov/cps/definitions.htm
- **synonym**: involuntary part-time population
- **synonym**: population employed part-time for economic reasons

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
