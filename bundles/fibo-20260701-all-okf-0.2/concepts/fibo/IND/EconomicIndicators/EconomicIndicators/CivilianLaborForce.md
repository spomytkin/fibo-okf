---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: civilian labor force
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the civilian, non-institutional population considered to be part of the labor force during a given reporting
      period
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: civilian labor force
type: Ontology Class
---

# civilian labor force

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce>

## Definition

subset of the civilian, non-institutional population considered to be part of the labor force during a given reporting period

## Relationships

- **Subclass of**: [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Constraints

- **Disjoint with**: [PopulationNotInLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/PopulationNotInLaborForce.md)

## Annotations

- **label**: civilian labor force
- **definition**: subset of the civilian, non-institutional population considered to be part of the labor force during a given reporting period
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
