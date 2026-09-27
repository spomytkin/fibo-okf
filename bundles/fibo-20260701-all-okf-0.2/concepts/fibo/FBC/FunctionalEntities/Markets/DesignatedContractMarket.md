---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: designated contract market
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: exchange, trading system, or platform that enables listing for trading futures or option contracts based on any
      underlying commodity, index or instrument
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DCM
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.cftc.gov/IndustryOversight/TradingOrganizations/DCMs/index.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-DCMS
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DesignatedContractMarket
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: designated contract market
type: Ontology Class
---

# designated contract market

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DesignatedContractMarket>

## Definition

exchange, trading system, or platform that enables listing for trading futures or option contracts based on any underlying commodity, index or instrument

## Relationships

- **Subclass of**: [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-DCMS`

## Annotations

- **label**: designated contract market
- **definition**: exchange, trading system, or platform that enables listing for trading futures or option contracts based on any underlying commodity, index or instrument
- **abbreviation**: DCM
- **adaptedFrom**: http://www.cftc.gov/IndustryOversight/TradingOrganizations/DCMs/index.htm
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
