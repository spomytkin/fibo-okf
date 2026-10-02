---
owl:
  annotations:
  - language: en-GB
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: organised trading facility
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: organized trading facility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: multi-lateral system which is not an RM or an MTF and in which multiple third-party buying and selling interests
      in bonds, structured finance products, emission allowances or derivatives are able to interact in the system in a way
      that results in a contract in accordance with the provisions of Title II of MiFID II
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: OTF
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.marketswiki.com/mwiki/Organized_Trading_Facility
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'OTFs were introduced by the European Commission as part of MiFID II and are focused on non-equities such as derivatives
      and cash bond markets.


      OTFs are intended to be similar in scope to a swap execution facility (SEF), a type of entity created by the Dodd-Frank
      Act in the U.S. The goal of SEFs and OTFs is to bring transparency and structure to OTC derivatives trading.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Unlike RMs and MTFs, operators of OTFs will have discretion as to how to execute orders, subject to pre-transparency
      and best execution obligations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-OTFS
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.financierworldwide.com/organised-trading-facilities-how-they-differ-from-mtfs
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OrganizedTradingFacility
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: organised trading facility
type: Ontology Class
---

# organised trading facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OrganizedTradingFacility>

## Definition

multi-lateral system which is not an RM or an MTF and in which multiple third-party buying and selling interests in bonds, structured finance products, emission allowances or derivatives are able to interact in the system in a way that results in a contract in accordance with the provisions of Title II of MiFID II

## Relationships

- **See also**: [organised-trading-facilities-how-they-differ-from-mtfs](<https://www.financierworldwide.com/organised-trading-facilities-how-they-differ-from-mtfs>)
- **Subclass of**: [AlternativeTradingSystem](/concepts/fibo/FBC/FunctionalEntities/Markets/AlternativeTradingSystem.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-OTFS`
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: all values from of type [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label** (en-GB): organised trading facility
- **label** (en-US): organized trading facility
- **definition**: multi-lateral system which is not an RM or an MTF and in which multiple third-party buying and selling interests in bonds, structured finance products, emission allowances or derivatives are able to interact in the system in a way that results in a contract in accordance with the provisions of Title II of MiFID II
- **abbreviation**: OTF
- **adaptedFrom**: http://www.marketswiki.com/mwiki/Organized_Trading_Facility
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **explanatoryNote**: OTFs were introduced by the European Commission as part of MiFID II and are focused on non-equities such as derivatives and cash bond markets.  OTFs are intended to be similar in scope to a swap execution facility (SEF), a type of entity created by the Dodd-Frank Act in the U.S. The goal of SEFs and OTFs is to bring transparency and structure to OTC derivatives trading.
- **explanatoryNote**: Unlike RMs and MTFs, operators of OTFs will have discretion as to how to execute orders, subject to pre-transparency and best execution obligations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
