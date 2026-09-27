---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employed population part-time
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week based
      on usual working hours
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/Index.aspx?DatasetCode=STLABOUR
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the U.S., part-time workers are those who usually work fewer than 35 hours per week. See https://www.bls.gov/cps/definitions.htm
      for additional details.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The definition of part-time varies considerably from country to country according to the OECD. Classification may
      be based on (1) employee perception, (2) usual working hours, which is the most reliable measure, or (3) actual working
      hours, which varies due to holidays, illness, etc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: population employed part-time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: employed population part-time
type: Ontology Class
---

# employed population part-time

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime>

## Definition

subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week based on usual working hours

## Relationships

- **Subclass of**: [EmployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md)

## Annotations

- **label**: employed population part-time
- **definition**: subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week based on usual working hours
- **adaptedFrom**: https://stats.oecd.org/Index.aspx?DatasetCode=STLABOUR
- **explanatoryNote**: In the U.S., part-time workers are those who usually work fewer than 35 hours per week. See https://www.bls.gov/cps/definitions.htm for additional details.
- **explanatoryNote**: The definition of part-time varies considerably from country to country according to the OECD. Classification may be based on (1) employee perception, (2) usual working hours, which is the most reliable measure, or (3) actual working hours, which varies due to holidays, illness, etc.
- **synonym**: population employed part-time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
