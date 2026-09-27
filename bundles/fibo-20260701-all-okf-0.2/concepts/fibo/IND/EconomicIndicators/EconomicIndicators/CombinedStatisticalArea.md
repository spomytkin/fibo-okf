---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: combined statistical area
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: combination of adjacent metropolitan and micropolitan areas with economic ties measured by commuting patterns
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CSA
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These areas that combine retain their own designations as metropolitan or micropolitan statistical areas within
      the larger combined statistical area.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  related_to:
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://en.wikipedia.org/wiki/Combined_statistical_area
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/fedreg_2010/06282010_metro_standards-Complete.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    resource: https://www.federalregister.gov/documents/2021/07/16/2021-15159/2020-standards-for-delineating-core-based-statistical-areas
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CombinedStatisticalArea
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: combined statistical area
type: Ontology Class
---

# combined statistical area

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CombinedStatisticalArea>

## Definition

combination of adjacent metropolitan and micropolitan areas with economic ties measured by commuting patterns

## Relationships

- **Related to**: [Combined_statistical_area](<https://en.wikipedia.org/wiki/Combined_statistical_area>)
- **Related to**: [06282010_metro_standards-Complete.pdf](<https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/fedreg_2010/06282010_metro_standards-Complete.pdf>)
- **Related to**: [2020-standards-for-delineating-core-based-statistical-areas](<https://www.federalregister.gov/documents/2021/07/16/2021-15159/2020-standards-for-delineating-core-based-statistical-areas>)
- **Subclass of**: [GovernmentSpecifiedStatisticalArea](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 2 of type [GovernmentSpecifiedStatisticalArea](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/GovernmentSpecifiedStatisticalArea.md)

## Annotations

- **label**: combined statistical area
- **definition**: combination of adjacent metropolitan and micropolitan areas with economic ties measured by commuting patterns
- **abbreviation**: CSA
- **explanatoryNote**: These areas that combine retain their own designations as metropolitan or micropolitan statistical areas within the larger combined statistical area.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
