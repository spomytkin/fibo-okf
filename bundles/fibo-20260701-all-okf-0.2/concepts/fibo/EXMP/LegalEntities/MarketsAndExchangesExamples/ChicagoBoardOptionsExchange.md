---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Chicago Board Options Exchange
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Chicago Board Options Exchange operating-level market founded in 1973 that is the world's largest options market
      with contracts focusing on individual equities, indexes, and interest rates
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: CBOE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: Chicago Board Options Exchange
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.cboe.com/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchangeAsServiceProvider.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchangeAsServiceProvider
  - concept: /concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchangeDateEstablished.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/hasDateEstablished
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchangeDateEstablished
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Chicago.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Chicago
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  same_as:
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCBO.md
    predicate: http://www.w3.org/2002/07/owl#sameAs
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCBO
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchange
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: Chicago Board Options Exchange
type: Ontology Individual
---

# Chicago Board Options Exchange

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchange>

## Definition

Chicago Board Options Exchange operating-level market founded in 1973 that is the world's largest options market with contracts focusing on individual equities, indexes, and interest rates

## Relationships

- **Related to**: [ChicagoBoardOptionsExchangeDateEstablished](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchangeDateEstablished.md)
- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Chicago](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Chicago.md)
- **Related to**: [ChicagoBoardOptionsExchangeAsServiceProvider](/concepts/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples/ChicagoBoardOptionsExchangeAsServiceProvider.md)
- **Same as**: [Facility-XCBO](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XCBO.md)

## Annotations

- **label**: Chicago Board Options Exchange
- **definition**: Chicago Board Options Exchange operating-level market founded in 1973 that is the world's largest options market with contracts focusing on individual equities, indexes, and interest rates
- **hasFacilityAcronym**: CBOE
- **hasFormalName**: Chicago Board Options Exchange
- **hasWebsite**: https://www.cboe.com/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
