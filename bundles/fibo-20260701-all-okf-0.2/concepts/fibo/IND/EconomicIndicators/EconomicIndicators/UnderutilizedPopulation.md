---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underutilized population
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the civilian non-institutional population that includes persons employed part-time for economic reasons,
      persons that are marginally attached to the labor force, and persons that are identified as unemployed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/news.release/empsit.t15.htm
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnderutilizedPopulation
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: underutilized population
type: Ontology Class
---

# underutilized population

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnderutilizedPopulation>

## Definition

subset of the civilian non-institutional population that includes persons employed part-time for economic reasons, persons that are marginally attached to the labor force, and persons that are identified as unemployed

## Relationships

- **Subclass of**: [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Annotations

- **label**: underutilized population
- **definition**: subset of the civilian non-institutional population that includes persons employed part-time for economic reasons, persons that are marginally attached to the labor force, and persons that are identified as unemployed
- **adaptedFrom**: https://www.bls.gov/news.release/empsit.t15.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
