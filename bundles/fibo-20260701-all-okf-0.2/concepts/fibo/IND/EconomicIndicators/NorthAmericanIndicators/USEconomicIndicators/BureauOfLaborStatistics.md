---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bureau of Labor Statistics
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the Bureau of Labor Statistics, the principal Federal agency responsible for measuring labor market activity, working
      conditions, and price changes in the economy
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BLS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.bls.gov/bls/infohome.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Its mission is to collect, analyze, and disseminate essential economic information to support public and private
      decision-making. As an independent statistical agency, BLS serves its diverse user communities by providing products
      and services that are objective, timely, accurate, and relevant.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency
  related_to:
  - concept: /concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UnitedStatesDepartmentOfLabor.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UnitedStatesDepartmentOfLabor
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.bls.gov/
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics
sources:
- id: fibo-source-6226f57562
  resource: references/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
  sha256: 6226f575629a4ee3c82b410564a799468e4879a8b2bae96e935c7a0a0ed2c6ac
  title: FIBO source IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators.rdf
title: Bureau of Labor Statistics
type: Ontology Individual
---

# Bureau of Labor Statistics

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics>

## Definition

the Bureau of Labor Statistics, the principal Federal agency responsible for measuring labor market activity, working conditions, and price changes in the economy

## Relationships

- **Related to**: [UnitedStatesDepartmentOfLabor](/concepts/fibo/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UnitedStatesDepartmentOfLabor.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **See also**: [http://www.bls.gov/](<http://www.bls.gov/>)

## Annotations

- **label**: Bureau of Labor Statistics
- **definition**: the Bureau of Labor Statistics, the principal Federal agency responsible for measuring labor market activity, working conditions, and price changes in the economy
- **abbreviation**: BLS
- **adaptedFrom**: http://www.bls.gov/bls/infohome.htm
- **explanatoryNote**: Its mission is to collect, analyze, and disseminate essential economic information to support public and private decision-making. As an independent statistical agency, BLS serves its diverse user communities by providing products and services that are objective, timely, accurate, and relevant.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
