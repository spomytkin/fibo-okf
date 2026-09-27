---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NYSE American Options
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: NYSE (New York Stock Exchange) American Options segment-level market that is an options trading platform under
      the name AMEX options exchange which facilitates trading of the options on domestic stocks; American depository receipts;
      broad-based, industry sector, and international indexes; exchange traded funds; HOLDRS; LEAPS; and equity and index
      FLEX options
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: American Stock Exchange
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasPriorLegalName
    value: NYSE Amex Options
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NYSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NYSE American Options
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.nyse.com/markets/american-options
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptionsAsServiceProvider.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptionsAsServiceProvider
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptionsDateEstablished.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptionsDateEstablished
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  same_as:
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-AMXO.md
    predicate: http://www.w3.org/2002/07/owl#sameAs
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-AMXO
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptions
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: NYSE American Options
type: Ontology Individual
---

# NYSE American Options

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptions>

## Definition

NYSE (New York Stock Exchange) American Options segment-level market that is an options trading platform under the name AMEX options exchange which facilitates trading of the options on domestic stocks; American depository receipts; broad-based, industry sector, and international indexes; exchange traded funds; HOLDRS; LEAPS; and equity and index FLEX options

## Relationships

- **Related to**: [NYSEAmericanOptionsDateEstablished](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptionsDateEstablished.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [NewYorkStockExchange](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchange.md)
- **Related to**: [NYSEAmericanOptionsAsServiceProvider](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/NYSEAmericanOptionsAsServiceProvider.md)
- **Same as**: [Facility-AMXO](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-AMXO.md)

## Annotations

- **label**: NYSE American Options
- **definition**: NYSE (New York Stock Exchange) American Options segment-level market that is an options trading platform under the name AMEX options exchange which facilitates trading of the options on domestic stocks; American depository receipts; broad-based, industry sector, and international indexes; exchange traded funds; HOLDRS; LEAPS; and equity and index FLEX options
- **hasPriorLegalName**: American Stock Exchange
- **hasPriorLegalName**: NYSE Amex Options
- **hasFacilityAcronym**: NYSE
- **hasFormalName**: NYSE American Options
- **hasWebsite**: https://www.nyse.com/markets/american-options

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
