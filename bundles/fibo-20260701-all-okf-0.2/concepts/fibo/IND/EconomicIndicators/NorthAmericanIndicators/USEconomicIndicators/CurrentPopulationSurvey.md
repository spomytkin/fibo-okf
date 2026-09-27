---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: current population survey
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: survey conducted on a regular basis that presents analytical information related to the general population of a
      given statistical area with respect to labor force, employment, unemployment, persons not in the labor force, hours
      of work, earnings, and other demographic and labor force characteristics
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: http://www.bls.gov/cps/
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/specifies
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/StatisticalProgram.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/StatisticalProgram
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentPopulationSurvey
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: current population survey
type: Ontology Class
---

# current population survey

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentPopulationSurvey>

## Definition

survey conducted on a regular basis that presents analytical information related to the general population of a given statistical area with respect to labor force, employment, unemployment, persons not in the labor force, hours of work, earnings, and other demographic and labor force characteristics

## Relationships

- **Related to**: [cps](<http://www.bls.gov/cps/>)
- **Subclass of**: [StatisticalProgram](/concepts/fibo/FND/Utilities/Analytics/StatisticalProgram.md)

## Constraints

- **[specifies](<https://www.omg.org/spec/Commons/Documents/specifies>)**: some values from of type [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Annotations

- **label**: current population survey
- **definition**: survey conducted on a regular basis that presents analytical information related to the general population of a given statistical area with respect to labor force, employment, unemployment, persons not in the labor force, hours of work, earnings, and other demographic and labor force characteristics

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
