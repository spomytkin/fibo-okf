---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exchange
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes,
      maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities,
      or other products, services, or goods, and includes the market place and facilities maintained by such exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10383, Securities and related financial instruments - Codes for exchanges and market identification (MIC),
      Third edition, 2012-10-01, confirmed 2018-03-29
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Securities Exchange Act of 1934, as amended 12 August 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'An exchange is typically a corporation or mutual organization that provides securities trading services, where
      securities may be bought and sold by third parties. As a facility, an exchange is also a place of trade associated with
      a particular site, i.e., stock exchange, regulated market such as an Electronic Trading Platform (ECN), or unregulated
      market, such as an Automated Trading System (ATS), or market data provider. Stock exchanges also provide facilities
      for the issue and redemption of securities as well as other financial instruments and capital events including the payment
      of income and dividends.


      The securities traded on a stock exchange include: shares issued by companies, unit trusts, derivatives, pooled investment
      products and bonds. To be able to trade a security on a certain stock exchange, it has to be listed there. Usually there
      is a central location at least for recordkeeping, but trade is less and less linked to such a physical place, as modern
      markets are electronic networks, which gives them advantages of speed and cost of transactions. Trade on an exchange
      is by members only.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: market
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
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListingService
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/provides
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/SitesAndFacilities/Facility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: exchange
type: Ontology Class
---

# exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange>

## Definition

any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes, maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities, or other products, services, or goods, and includes the market place and facilities maintained by such exchange

## Relationships

- **Subclass of**: [Facility](<https://www.omg.org/spec/Commons/SitesAndFacilities/Facility>)

## Constraints

- **[hasFacilityAcronym](/concepts/fibo/FBC/FunctionalEntities/Markets/hasFacilityAcronym.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[operatesInCountry](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInCountry.md)**: some values from of type [Country](<https://www.omg.org/spec/Commons/Locations/Country>)
- **[operatesInMunicipality](/concepts/fibo/FBC/FunctionalEntities/Markets/operatesInMunicipality.md)**: some values from of type [Municipality](<https://www.omg.org/spec/Commons/Locations/Municipality>)
- **[hasFormalName](/concepts/fibo/FND/Relations/Relations/hasFormalName.md)**: min qualified cardinality 0 of type [Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: min qualified cardinality 0 of type [MarketIdentifier](/concepts/fibo/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: min qualified cardinality 0 of type [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- **[provides](<https://www.omg.org/spec/Commons/Organizations/provides>)**: some values from of type [ListingService](/concepts/fibo/SEC/Securities/SecuritiesListings/ListingService.md)

## Annotations

- **label**: exchange
- **definition**: any organization, association, or group of persons, whether incorporated or unincorporated, which constitutes, maintains, or provides a facility for bringing together purchasers and sellers of financial instruments, commodities, or other products, services, or goods, and includes the market place and facilities maintained by such exchange
- **adaptedFrom**: ISO 10383, Securities and related financial instruments - Codes for exchanges and market identification (MIC), Third edition, 2012-10-01, confirmed 2018-03-29
- **adaptedFrom**: Securities Exchange Act of 1934, as amended 12 August 2012
- **explanatoryNote**: An exchange is typically a corporation or mutual organization that provides securities trading services, where securities may be bought and sold by third parties. As a facility, an exchange is also a place of trade associated with a particular site, i.e., stock exchange, regulated market such as an Electronic Trading Platform (ECN), or unregulated market, such as an Automated Trading System (ATS), or market data provider. Stock exchanges also provide facilities for the issue and redemption of securities as well as other financial instruments and capital events including the payment of income and dividends.  The securities traded on a stock exchange include: shares issued by companies, unit trusts, derivatives, pooled investment products and bonds. To be able to trade a security on a certain stock exchange, it has to be listed there. Usually there is a central location at least for recordkeeping, but trade is less and less linked to such a physical place, as modern markets are electronic networks, which gives them advantages of speed and cost of transactions. Trade on an exchange is by members only.
- **synonym**: market

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
