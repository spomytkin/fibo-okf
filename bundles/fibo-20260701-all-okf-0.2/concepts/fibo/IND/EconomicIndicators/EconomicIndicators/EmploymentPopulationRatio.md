---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employment-population ratio
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing the ratio of the employed population with respect to the overall civilian non-institutional
      population of a given economy for some specified period
  - predicate: https://www.omg.org/spec/Commons/QuantitiesAndUnits/describesActualExpression
    value: employed population ÷ civilian non-institutional population
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.bls.gov/news.release/pdf/empsit.pdf
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmploymentPopulationRatio
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: employment-population ratio
type: Ontology Class
---

# employment-population ratio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmploymentPopulationRatio>

## Definition

economic indicator representing the ratio of the employed population with respect to the overall civilian non-institutional population of a given economy for some specified period

## Relationships

- **See also**: [empsit.pdf](<http://www.bls.gov/news.release/pdf/empsit.pdf>)
- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **[hasBaselinePopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation.md)**: some values from of type [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)
- **[hasComparisonPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasComparisonPopulation.md)**: some values from of type [EmployedPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmployedPopulation.md)

## Annotations

- **label**: employment-population ratio
- **definition**: economic indicator representing the ratio of the employed population with respect to the overall civilian non-institutional population of a given economy for some specified period
- **describesActualExpression**: employed population ÷ civilian non-institutional population

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
