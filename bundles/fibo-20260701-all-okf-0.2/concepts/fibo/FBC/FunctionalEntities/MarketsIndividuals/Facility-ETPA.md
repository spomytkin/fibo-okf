---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ENERGY TRADING PLATFORM AMSTERDAM
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ELECTRONIC PLATFORM TO TRADE SPOT ENERGY CONTRACTS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ETPA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: ENERGY TRADING PLATFORM AMSTERDAM
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.etpa.nl
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Amsterdam.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Amsterdam
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-724500ESIIL4H59L4375.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-724500ESIIL4H59L4375
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ETPA
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: ENERGY TRADING PLATFORM AMSTERDAM
type: Ontology Individual
---

# ENERGY TRADING PLATFORM AMSTERDAM

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ETPA>

## Relationships

- **Related to**: [Netherlands](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands>)
- **Related to**: [Amsterdam](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Amsterdam.md)
- **Related to**: [ServiceProvider-L-724500ESIIL4H59L4375](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-724500ESIIL4H59L4375.md)

## Annotations

- **label**: ENERGY TRADING PLATFORM AMSTERDAM
- **note**: ELECTRONIC PLATFORM TO TRADE SPOT ENERGY CONTRACTS.
- **hasFacilityAcronym**: ETPA
- **hasFormalName**: ENERGY TRADING PLATFORM AMSTERDAM
- **hasWebsite**: http://www.etpa.nl

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
