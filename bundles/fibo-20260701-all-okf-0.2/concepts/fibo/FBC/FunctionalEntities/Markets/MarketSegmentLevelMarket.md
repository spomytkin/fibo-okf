---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market segment-level market
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: section of an exchange/market/trade reporting facility that specialises in one or more specific instruments or
      that is regulated differently
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Dark pool
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: A market segment MIC can only be registered if an operating/exchange MIC already exists.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: It is not required to have a MIC registered for all segments of a market, only for those segments that need to
      be identified.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10383, Securities and related financial instruments - Codes for exchanges and market identification (MIC),
      Third edition, 2012-10-01, confirmed 2018-03-29, clause 2.2
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketLevelClassifier-SGMT
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: market segment-level market
type: Ontology Class
---

# market segment-level market

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket>

## Definition

section of an exchange/market/trade reporting facility that specialises in one or more specific instruments or that is regulated differently

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketLevelClassifier-SGMT`
- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from of type [OperatingLevelMarket](/concepts/fibo/FBC/FunctionalEntities/Markets/OperatingLevelMarket.md)

## Annotations

- **label**: market segment-level market
- **definition**: section of an exchange/market/trade reporting facility that specialises in one or more specific instruments or that is regulated differently
- **example**: Dark pool
- **note**: A market segment MIC can only be registered if an operating/exchange MIC already exists.
- **note**: It is not required to have a MIC registered for all segments of a market, only for those segments that need to be identified.
- **adaptedFrom**: ISO 10383, Securities and related financial instruments - Codes for exchanges and market identification (MIC), Third edition, 2012-10-01, confirmed 2018-03-29, clause 2.2
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
