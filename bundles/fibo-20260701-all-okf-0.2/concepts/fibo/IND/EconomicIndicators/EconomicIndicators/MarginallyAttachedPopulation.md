---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: marginally attached population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the population that includes people who currently are neither working nor looking for work but indicate
      that they want and are available for a job and have looked for work sometime in the past 12 months
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/news.release/empsit.t15.htm
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/MarginallyAttachedPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: marginally attached population
type: Ontology Class
---

# marginally attached population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/MarginallyAttachedPopulation>

## Definition

subset of the population that includes people who currently are neither working nor looking for work but indicate that they want and are available for a job and have looked for work sometime in the past 12 months

## Relationships

- **Subclass of**: [PopulationNotInLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce.md)

## Annotations

- **label**: marginally attached population
- **definition**: subset of the population that includes people who currently are neither working nor looking for work but indicate that they want and are available for a job and have looked for work sometime in the past 12 months
- **adaptedFrom**: https://www.bls.gov/news.release/empsit.t15.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
