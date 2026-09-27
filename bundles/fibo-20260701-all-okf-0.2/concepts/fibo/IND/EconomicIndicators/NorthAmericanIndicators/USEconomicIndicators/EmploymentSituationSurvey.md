---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employment situation survey
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a survey conducted on a regular basis that presents analytical information focused on the employment characteristics
      of a given statistical area
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: http://www.bls.gov/opub/reports/about.htm
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/isSeasonallyAdjusted
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentEmploymentStatistics.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentEmploymentStatistics
  - concept: /concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentPopulationSurvey.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentPopulationSurvey
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationSurvey
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: employment situation survey
type: Ontology Class
---

# employment situation survey

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/EmploymentSituationSurvey>

## Definition

a survey conducted on a regular basis that presents analytical information focused on the employment characteristics of a given statistical area

## Relationships

- **Related to**: [about.htm](<http://www.bls.gov/opub/reports/about.htm>)
- **Subclass of**: [CurrentEmploymentStatistics](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentEmploymentStatistics.md)
- **Subclass of**: [CurrentPopulationSurvey](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/CurrentPopulationSurvey.md)

## Constraints

- **[isSeasonallyAdjusted](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/isSeasonallyAdjusted.md)**: exact qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: employment situation survey
- **definition**: a survey conducted on a regular basis that presents analytical information focused on the employment characteristics of a given statistical area

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
