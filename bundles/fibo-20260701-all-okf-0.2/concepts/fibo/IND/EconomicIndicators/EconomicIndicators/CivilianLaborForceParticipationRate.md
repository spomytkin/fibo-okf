---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: civilian labor force participation rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing the rate of participation the labor force of a given economy for some specified
      period
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bls.gov/cps/definitions.htm#lfpr
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The labor force participation rate is the percentage of the population that is either employed or unemployed (that
      is, either working or actively seeking work).
  - predicate: https://www.omg.org/spec/Commons/QuantitiesAndUnits/describesActualExpression
    value: civilian labor force ÷ civilian non-institutional population
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForceParticipationRate
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: civilian labor force participation rate
type: Ontology Class
---

# civilian labor force participation rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForceParticipationRate>

## Definition

economic indicator representing the rate of participation the labor force of a given economy for some specified period

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasBaselinePopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation.md)**: some values from of type [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)
- **[hasComparisonPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation.md)**: some values from of type [CivilianLaborForce](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForce.md)

## Annotations

- **label**: civilian labor force participation rate
- **definition**: economic indicator representing the rate of participation the labor force of a given economy for some specified period
- **adaptedFrom**: https://www.bls.gov/cps/definitions.htm#lfpr
- **explanatoryNote**: The labor force participation rate is the percentage of the population that is either employed or unemployed (that is, either working or actively seeking work).
- **describesActualExpression**: civilian labor force ÷ civilian non-institutional population

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
