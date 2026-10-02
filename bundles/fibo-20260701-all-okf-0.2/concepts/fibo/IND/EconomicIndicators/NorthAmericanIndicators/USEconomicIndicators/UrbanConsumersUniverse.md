---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: urban consumers universe
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a statistical universe for consumer expenditure surveys consisting of people within a household that make joint
      expenditure decisions
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics, http://www.bls.gov/cpi/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, the CPI-U population, which covers about 88 percent of the U.S. population, covers households
      in all areas of the United States except people living in rural nonmetropolitan areas, in farm households, on military
      installations, in religious communities, and in institutions such as prisons and mental hospitals.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N5cc8876504cc4c6faf2a82c3f7b86c50
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/ConsumerExpenditureSurvey
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/PointOfPurchaseSurvey
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: urban consumers universe
type: Ontology Class
---

# urban consumers universe

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse>

## Definition

a statistical universe for consumer expenditure surveys consisting of people within a household that make joint expenditure decisions

## Relationships

- **Subclass of**: [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N5cc8876504cc4c6faf2a82c3f7b86c50`
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [ConsumerExpenditureSurvey](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/ConsumerExpenditureSurvey.md)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [PointOfPurchaseSurvey](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/PointOfPurchaseSurvey.md)

## Annotations

- **label**: urban consumers universe
- **definition**: a statistical universe for consumer expenditure surveys consisting of people within a household that make joint expenditure decisions
- **adaptedFrom**: U.S. Bureau of Labor Statistics, http://www.bls.gov/cpi/
- **explanatoryNote**: In the United States, the CPI-U population, which covers about 88 percent of the U.S. population, covers households in all areas of the United States except people living in rural nonmetropolitan areas, in farm households, on military installations, in religious communities, and in institutions such as prisons and mental hospitals.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
