---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underemployed population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the employed population that includes persons employed part-time for economic reasons, who want and are
      available for full-time work but have had to settle for a part-time schedule
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/news.release/empsit.t15.htm
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnderemployedPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: underemployed population
type: Ontology Class
---

# underemployed population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnderemployedPopulation>

## Definition

subset of the employed population that includes persons employed part-time for economic reasons, who want and are available for full-time work but have had to settle for a part-time schedule

## Relationships

- **Subclass of**: [EmployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md)

## Annotations

- **label**: underemployed population
- **definition**: subset of the employed population that includes persons employed part-time for economic reasons, who want and are available for full-time work but have had to settle for a part-time schedule
- **adaptedFrom**: https://www.bls.gov/news.release/empsit.t15.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
