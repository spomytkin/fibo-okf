---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: multilateral trading facility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trading system that facilitates the exchange of financial instruments between multiple parties
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MTF
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/m/multilateral_trading_facility.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Multilateral trading facilities allow eligible contract participants to gather and transfer a variety of securities,
      especially instruments that may not have an official market. These facilities are often electronic systems controlled
      by approved market operators or larger investment banks. Traders will usually submit orders electronically, where a
      matching software engine is used to pair buyers with sellers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-MLTF
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: multilateral trading facility
type: Ontology Class
---

# multilateral trading facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility>

## Definition

trading system that facilitates the exchange of financial instruments between multiple parties

## Relationships

- **Subclass of**: [AlternativeTradingSystem](/concepts/fibo/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-MLTF`

## Annotations

- **label**: multilateral trading facility
- **definition**: trading system that facilitates the exchange of financial instruments between multiple parties
- **abbreviation**: MTF
- **adaptedFrom**: http://www.investopedia.com/terms/m/multilateral_trading_facility.asp
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **explanatoryNote**: Multilateral trading facilities allow eligible contract participants to gather and transfer a variety of securities, especially instruments that may not have an official market. These facilities are often electronic systems controlled by approved market operators or larger investment banks. Traders will usually submit orders electronically, where a matching software engine is used to pair buyers with sellers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
