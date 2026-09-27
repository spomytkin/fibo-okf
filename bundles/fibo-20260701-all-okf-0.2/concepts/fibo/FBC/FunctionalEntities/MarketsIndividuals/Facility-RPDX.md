---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MOSCOW ENERGY EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: RUSSIAN POWER DERIVATIVES EXCHANGE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: MOSENEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MOSCOW ENERGY EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.mosenex.ru
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Moscow.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Moscow
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MOSCOWENERGYEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MOSCOWENERGYEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-RPDX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MOSCOW ENERGY EXCHANGE
type: Ontology Individual
---

# MOSCOW ENERGY EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-RPDX>

## Relationships

- **Related to**: [RussianFederation](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation>)
- **Related to**: [Moscow](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Moscow.md)
- **Related to**: [ServiceProvider-MOSCOWENERGYEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MOSCOWENERGYEXCHANGE.md)

## Annotations

- **label**: MOSCOW ENERGY EXCHANGE
- **note**: RUSSIAN POWER DERIVATIVES EXCHANGE.
- **hasFacilityAcronym**: MOSENEX
- **hasFormalName**: MOSCOW ENERGY EXCHANGE
- **hasWebsite**: http://www.mosenex.ru

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
