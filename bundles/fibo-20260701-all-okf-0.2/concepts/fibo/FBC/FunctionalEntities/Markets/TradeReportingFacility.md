---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trade reporting facility
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: facility that provides a mechanism for the reporting of transactions effected otherwise than on an exchange
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: In the United States, for example, trades by FINRA members in Nasdaq-listed and other exchange-listed securities,
      as approved by the Securities and Exchange Commission (SEC), executed otherwise than on an exchange may be reported
      to a FINRA TRF. While each FINRA TRF is affiliated with a registered national securities exchange, each FINRA TRF is
      a FINRA facility and is subject to FINRA's registration as a national securities association.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: TRF
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.finra.org/filing-reporting/trade-reporting-facility-trf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
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
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-TRFS
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/SitesAndFacilities/Facility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/TradeReportingFacility
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: trade reporting facility
type: Ontology Class
---

# trade reporting facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/TradeReportingFacility>

## Definition

facility that provides a mechanism for the reporting of transactions effected otherwise than on an exchange

## Relationships

- **Subclass of**: [Facility](<https://www.omg.org/spec/Commons/SitesAndFacilities/Facility>)

## Constraints

- **[hasFacilityAcronym](/concepts/fibo/FBC/FunctionalEntities/Markets/hasFacilityAcronym.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[operatesInCountry](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInCountry.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[operatesInMunicipality](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInMunicipality.md)**: some values from of type [Municipality](<https://www.omg.org/spec/Commons/Locations/Municipality>)
- **[hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketCategoryClassifier-TRFS`
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [MarketIdentifier](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: min qualified cardinality 0 of type [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Annotations

- **label**: trade reporting facility
- **definition**: facility that provides a mechanism for the reporting of transactions effected otherwise than on an exchange
- **example**: In the United States, for example, trades by FINRA members in Nasdaq-listed and other exchange-listed securities, as approved by the Securities and Exchange Commission (SEC), executed otherwise than on an exchange may be reported to a FINRA TRF. While each FINRA TRF is affiliated with a registered national securities exchange, each FINRA TRF is a FINRA facility and is subject to FINRA's registration as a national securities association.
- **abbreviation**: TRF
- **adaptedFrom**: https://www.finra.org/filing-reporting/trade-reporting-facility-trf
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
