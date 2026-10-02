---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MOSCOW EXCHANGE - ALL MARKETS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: EQUITIES, BONDS, CURRENCIES, MONEY MARKET INSTRUMENTS, COMMODITIES AND MOEX BOARD.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MOEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MOSCOW EXCHANGE - ALL MARKETS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.moex.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Moscow.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Moscow
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-253400M5M1222KPNWE87.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-253400M5M1222KPNWE87
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MISX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MOSCOW EXCHANGE - ALL MARKETS
type: Ontology Individual
---

# MOSCOW EXCHANGE - ALL MARKETS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MISX>

## Relationships

- **Related to**: [RussianFederation](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation>)
- **Related to**: [Moscow](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Moscow.md)
- **Related to**: [ServiceProvider-L-253400M5M1222KPNWE87](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-253400M5M1222KPNWE87.md)

## Annotations

- **label**: MOSCOW EXCHANGE - ALL MARKETS
- **note**: EQUITIES, BONDS, CURRENCIES, MONEY MARKET INSTRUMENTS, COMMODITIES AND MOEX BOARD.
- **hasFacilityAcronym**: MOEX
- **hasFormalName**: MOSCOW EXCHANGE - ALL MARKETS
- **hasWebsite**: http://www.moex.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
