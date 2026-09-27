---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: New York Stock Exchange
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: New York Stock Exchange operating-level market founded in 1792 that is a market place for trading of common stock
      and other securities
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NYSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: New York Stock Exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The New York Stock Exchange is a leading global cash equity exchange. It is the leading equity exchange for initial
      public offerings, or IPOs, globally, and enables companies seeking to raise capital to become publicly listed through
      the IPO process upon meeting exchange listing standards. In addition to common stocks, preferred stocks and warrants,
      the NYSE lists structured products, such as capital securities and mandatory convertible securities. In addition, NYSE
      operates NYSE Bonds, an electronic trading platform with transparent pricing for debt securities, including corporate
      bonds.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.nyse.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeAsServiceProvider.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeAsServiceProvider
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeDateEstablished.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeDateEstablished
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  same_as:
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS.md
    predicate: http://www.w3.org/2002/07/owl#sameAs
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: New York Stock Exchange
type: Ontology Individual
---

# New York Stock Exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange>

## Definition

New York Stock Exchange operating-level market founded in 1792 that is a market place for trading of common stock and other securities

## Relationships

- **Related to**: [NewYorkStockExchangeDateEstablished](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeDateEstablished.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [NewYorkStockExchangeAsServiceProvider](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeAsServiceProvider.md)
- **Same as**: [Facility-XNYS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS.md)

## Annotations

- **label**: New York Stock Exchange
- **definition**: New York Stock Exchange operating-level market founded in 1792 that is a market place for trading of common stock and other securities
- **hasFacilityAcronym**: NYSE
- **hasFormalName**: New York Stock Exchange
- **explanatoryNote**: The New York Stock Exchange is a leading global cash equity exchange. It is the leading equity exchange for initial public offerings, or IPOs, globally, and enables companies seeking to raise capital to become publicly listed through the IPO process upon meeting exchange listing standards. In addition to common stocks, preferred stocks and warrants, the NYSE lists structured products, such as capital securities and mandatory convertible securities. In addition, NYSE operates NYSE Bonds, an electronic trading platform with transparent pricing for debt securities, including corporate bonds.
- **hasWebsite**: https://www.nyse.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
