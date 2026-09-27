---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: REGIONAL EXCHANGE CENTRE - MICEX VOLGA REGION
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: NNCS ORGANIZES THE TRADING (AND REPORTING) ON THE COMMODITY SESSION WHERE TRADES ARE EXECUTED SEPARATELY FROM THE
      MOSCOW OFFICE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NCSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: REGIONAL EXCHANGE CENTRE - MICEX VOLGA REGION
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.micex-pfo.ru
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Nizhniy_Novgorod.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Nizhniy_Novgorod
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-REGIONALEXCHANGECENTRE-MICEXVOLGAREGION.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-REGIONALEXCHANGECENTRE-MICEXVOLGAREGION
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NNCS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: REGIONAL EXCHANGE CENTRE - MICEX VOLGA REGION
type: Ontology Individual
---

# REGIONAL EXCHANGE CENTRE - MICEX VOLGA REGION

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NNCS>

## Relationships

- **Related to**: [RussianFederation](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation>)
- **Related to**: [Nizhniy_Novgorod](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Nizhniy_Novgorod.md)
- **Related to**: [ServiceProvider-REGIONALEXCHANGECENTRE-MICEXVOLGAREGION](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-REGIONALEXCHANGECENTRE-MICEXVOLGAREGION.md)

## Annotations

- **label**: REGIONAL EXCHANGE CENTRE - MICEX VOLGA REGION
- **note**: NNCS ORGANIZES THE TRADING (AND REPORTING) ON THE COMMODITY SESSION WHERE TRADES ARE EXECUTED SEPARATELY FROM THE MOSCOW OFFICE.
- **hasFacilityAcronym**: NCSE
- **hasFormalName**: REGIONAL EXCHANGE CENTRE - MICEX VOLGA REGION
- **hasWebsite**: http://www.micex-pfo.ru

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
