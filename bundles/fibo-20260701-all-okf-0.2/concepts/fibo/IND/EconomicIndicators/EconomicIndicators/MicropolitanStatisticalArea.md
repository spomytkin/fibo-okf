---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: micropolitan statistical area
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: one or more adjacent counties or county equivalents that have at least one urban core area of at least 10,000 population
      but less than 50,000, plus adjacent territory that has a high degree of social and economic integration with the core
      as measured by commuting ties
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: μSA
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://en.wikipedia.org/wiki/List_of_micropolitan_statistical_areas
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/fedreg_2010/06282010_metro_standards-Complete.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://www.federalregister.gov/documents/2021/07/16/2021-15159/2020-standards-for-delineating-core-based-statistical-areas
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/MicropolitanStatisticalArea
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: micropolitan statistical area
type: Ontology Class
---

# micropolitan statistical area

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/MicropolitanStatisticalArea>

## Definition

one or more adjacent counties or county equivalents that have at least one urban core area of at least 10,000 population but less than 50,000, plus adjacent territory that has a high degree of social and economic integration with the core as measured by commuting ties

## Relationships

- **Related to**: [List_of_micropolitan_statistical_areas](<https://en.wikipedia.org/wiki/List_of_micropolitan_statistical_areas>)
- **Related to**: [06282010_metro_standards-Complete.pdf](<https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/fedreg_2010/06282010_metro_standards-Complete.pdf>)
- **Related to**: [2020-standards-for-delineating-core-based-statistical-areas](<https://www.federalregister.gov/documents/2021/07/16/2021-15159/2020-standards-for-delineating-core-based-statistical-areas>)
- **Subclass of**: [GovernmentSpecifiedStatisticalArea](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md)

## Annotations

- **label**: micropolitan statistical area
- **definition**: one or more adjacent counties or county equivalents that have at least one urban core area of at least 10,000 population but less than 50,000, plus adjacent territory that has a high degree of social and economic integration with the core as measured by commuting ties
- **abbreviation**: μSA

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
