---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employed population part-time for non-economic reasons
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week due
      to illness or other health or medical limitations, childcare problems, family or personal obligations, being in school
      or training, retirement or Social Security limits on earnings, and having a job where full-time work is less than 35
      hours
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/cps/definitions.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: population employed part-time for non-economic reasons
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForEconomicReasons.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForEconomicReasons
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForNonEconomicReasons
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: employed population part-time for non-economic reasons
type: Ontology Class
---

# employed population part-time for non-economic reasons

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForNonEconomicReasons>

## Definition

subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week due to illness or other health or medical limitations, childcare problems, family or personal obligations, being in school or training, retirement or Social Security limits on earnings, and having a job where full-time work is less than 35 hours

## Relationships

- **Subclass of**: [EmployedPopulationPartTime](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTime.md)

## Constraints

- **Disjoint with**: [EmployedPopulationPartTimeForEconomicReasons](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulationPartTimeForEconomicReasons.md)

## Annotations

- **label**: employed population part-time for non-economic reasons
- **definition**: subset of the employed population that includes persons that are working fewer than 30 to 35 hours per week due to illness or other health or medical limitations, childcare problems, family or personal obligations, being in school or training, retirement or Social Security limits on earnings, and having a job where full-time work is less than 35 hours
- **adaptedFrom**: https://www.bls.gov/cps/definitions.htm
- **synonym**: population employed part-time for non-economic reasons

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
