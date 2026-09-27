---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NYSE Arca
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: NYSE Arca functional entity that is an electronic stock market, supporting trading of equity securities and options
      products listed in the United States, including trading exchange-traded funds (ETFs) and exchange-listed securities
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: The Archipelago Exchange
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NYSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NYSE Arca
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.nyse.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArcaAsServiceProvider.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArcaAsServiceProvider
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArcaDateEstablished.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArcaDateEstablished
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Chicago.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Chicago
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  same_as:
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-ARCX.md
    predicate: http://www.w3.org/2002/07/owl#sameAs
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ARCX
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArca
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: NYSE Arca
type: Ontology Individual
---

# NYSE Arca

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArca>

## Definition

NYSE Arca functional entity that is an electronic stock market, supporting trading of equity securities and options products listed in the United States, including trading exchange-traded funds (ETFs) and exchange-listed securities

## Relationships

- **Related to**: [NYSEArcaDateEstablished](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArcaDateEstablished.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Chicago](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Chicago.md)
- **Related to**: [NewYorkStockExchange](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md)
- **Related to**: [NYSEArcaAsServiceProvider](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEArcaAsServiceProvider.md)
- **Same as**: [Facility-ARCX](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-ARCX.md)

## Annotations

- **label**: NYSE Arca
- **definition**: NYSE Arca functional entity that is an electronic stock market, supporting trading of equity securities and options products listed in the United States, including trading exchange-traded funds (ETFs) and exchange-listed securities
- **hasPriorLegalName**: The Archipelago Exchange
- **hasFacilityAcronym**: NYSE
- **hasFormalName**: NYSE Arca
- **hasWebsite**: https://www.nyse.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
