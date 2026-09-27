---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: data reporting services provider
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: market data provider and reporting party that reports and/or publishes data on securities transactions, including
      required regulatory reporting for such transactions, and as such is subject to regulatory supervision
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DRSP
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.esma.europa.eu/press-news/esma-news/esma-identifies-data-reporting-services-providers-be-supervised-directly
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.esma.europa.eu/supervision/supervision/data-reporting-services-providers
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
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/MarketDataProvider
  - concept: /concepts/fibo/FND/Arrangements/Reporting/ReportingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/ReportingParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DataReportingServicesProvider
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: data reporting services provider
type: Ontology Class
---

# data reporting services provider

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DataReportingServicesProvider>

## Definition

market data provider and reporting party that reports and/or publishes data on securities transactions, including required regulatory reporting for such transactions, and as such is subject to regulatory supervision

## Relationships

- **Subclass of**: [MarketDataProvider](/concepts/fibo/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
- **Subclass of**: [ReportingParty](/concepts/fibo/FND/Arrangements/Reporting/ReportingParty.md)

## Constraints

- **[hasFacilityAcronym](/concepts/fibo/FBC/FunctionalEntities/Markets/hasFacilityAcronym.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[operatesInCountry](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInCountry.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[operatesInMunicipality](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInMunicipality.md)**: some values from of type [Municipality](<https://www.omg.org/spec/Commons/Locations/Municipality>)
- **[hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [MarketIdentifier](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifier.md)

## Annotations

- **label**: data reporting services provider
- **definition**: market data provider and reporting party that reports and/or publishes data on securities transactions, including required regulatory reporting for such transactions, and as such is subject to regulatory supervision
- **abbreviation**: DRSP
- **adaptedFrom**: https://www.esma.europa.eu/press-news/esma-news/esma-identifies-data-reporting-services-providers-be-supervised-directly
- **adaptedFrom**: https://www.esma.europa.eu/supervision/supervision/data-reporting-services-providers

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
