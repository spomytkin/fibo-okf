---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: crypto asset services provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial services provider that provides services for crypto assets that enable the control of crypto assets,
      and participate in, or provide, financial services for issuers' offers, or sale, of crypto assets
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CASP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/crypto-asset-service-provider-casp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Services related to crypto assets may include businesses that exchange crypto assets for fiat currencies, or vice
      versa, that conduct transactions that move crypto assets from one crypto asset address, or account, to another, and/or
      that provide facilities for the safekeeping, or administration, of crypto assets, or instruments.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
  - filler: https://www.omg.org/spec/Commons/Locations/Country
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
  - filler: https://www.omg.org/spec/Commons/Locations/Municipality
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
  - cardinality: 0
    filler: http://www.w3.org/2000/01/rdf-schema#Literal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-CASP
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/CryptoAssetServicesProvider
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: crypto asset services provider
type: Ontology Class
---

# crypto asset services provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/CryptoAssetServicesProvider>

## Definition

financial services provider that provides services for crypto assets that enable the control of crypto assets, and participate in, or provide, financial services for issuers' offers, or sale, of crypto assets

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Constraints

- **[hasFacilityAcronym](/concepts/fibo/FBC/FunctionalEntities/Markets/hasFacilityAcronym.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[operatesInCountry](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInCountry.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[operatesInMunicipality](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInMunicipality.md)**: some values from of type [Municipality](<https://www.omg.org/spec/Commons/Locations/Municipality>)
- **[hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-CASP`
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [MarketIdentifier](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifier.md)

## Annotations

- **label**: crypto asset services provider
- **definition**: financial services provider that provides services for crypto assets that enable the control of crypto assets, and participate in, or provide, financial services for issuers' offers, or sale, of crypto assets
- **abbreviation**: CASP
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **adaptedFrom**: https://www.lawinsider.com/dictionary/crypto-asset-service-provider-casp
- **explanatoryNote**: Services related to crypto assets may include businesses that exchange crypto assets for fiat currencies, or vice versa, that conduct transactions that move crypto assets from one crypto asset address, or account, to another, and/or that provide facilities for the safekeeping, or administration, of crypto assets, or instruments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
