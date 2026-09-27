---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consumer price index
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: economic indicator representing measure of the change over time in the prices of consumer goods and services that
      households consume
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CPI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://unstats.un.org/unsd/nationalaccount/docs/SNA2008.pdf
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.ilo.org/public/english/bureau/stat/guides/cpi/
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForceParticipationRate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForceParticipationRate
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmploymentPopulationRatio.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EmploymentPopulationRatio
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GrossDomesticProduct.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GrossDomesticProduct
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InflationRate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InflationRate
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/FixedBasket
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/hasInput
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: consumer price index
type: Ontology Class
---

# consumer price index

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex>

## Definition

economic indicator representing measure of the change over time in the prices of consumer goods and services that households consume

## Relationships

- **Subclass of**: [EconomicIndicator](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- **Subclass of**: [Expression](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Expression>)

## Constraints

- **Disjoint with**: [CivilianLaborForceParticipationRate](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianLaborForceParticipationRate.md)
- **Disjoint with**: [EmploymentPopulationRatio](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/EmploymentPopulationRatio.md)
- **Disjoint with**: [GrossDomesticProduct](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GrossDomesticProduct.md)
- **Disjoint with**: [InflationRate](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InflationRate.md)
- **Disjoint with**: [UnemploymentRate](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/UnemploymentRate.md)
- **[hasInput](/concepts/fibo/FND/DatesAndTimes/Occurrences/hasInput.md)**: some values from of type [FixedBasket](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md)
- **[hasBaselinePopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/hasBaselinePopulation.md)**: some values from of type [CivilianNonInstitutionalPopulation](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPopulation.md)

## Annotations

- **label**: consumer price index
- **definition**: economic indicator representing measure of the change over time in the prices of consumer goods and services that households consume
- **abbreviation**: CPI
- **adaptedFrom**: http://unstats.un.org/unsd/nationalaccount/docs/SNA2008.pdf
- **adaptedFrom**: http://www.ilo.org/public/english/bureau/stat/guides/cpi/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
