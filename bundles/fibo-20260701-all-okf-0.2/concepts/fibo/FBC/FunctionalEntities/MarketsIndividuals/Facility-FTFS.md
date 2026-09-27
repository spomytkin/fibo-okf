---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: 42 FINANCIAL SERVICES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: 42FS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: 42 FINANCIAL SERVICES
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.42fs.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OrganizedTradingFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Prague.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Prague
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-31570010000000050826.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-31570010000000050826
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Czechia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FTFS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: 42 FINANCIAL SERVICES
type: Ontology Individual
---

# 42 FINANCIAL SERVICES

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FTFS>

## Relationships

- **Related to**: [Czechia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Czechia>)
- **Related to**: [Prague](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Prague.md)
- **Related to**: [ServiceProvider-L-31570010000000050826](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-31570010000000050826.md)

## Annotations

- **label**: 42 FINANCIAL SERVICES
- **hasFacilityAcronym**: 42FS
- **hasFormalName**: 42 FINANCIAL SERVICES
- **hasWebsite**: http://www.42fs.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
