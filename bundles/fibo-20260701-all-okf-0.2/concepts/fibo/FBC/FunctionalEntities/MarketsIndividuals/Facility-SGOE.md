---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SG OPTION EUROPE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SG OPTION EUROPE - SYSTEMATIC INTERNALISER BUSINESSES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SGOE SI
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SG OPTION EUROPE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.sgcib.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-969500FDN8G43HMHZM83.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-969500FDN8G43HMHZM83
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/France
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SGOE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SG OPTION EUROPE
type: Ontology Individual
---

# SG OPTION EUROPE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SGOE>

## Relationships

- **Related to**: [France](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/France>)
- **Related to**: [Paris](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris.md)
- **Related to**: [ServiceProvider-L-969500FDN8G43HMHZM83](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-969500FDN8G43HMHZM83.md)

## Annotations

- **label**: SG OPTION EUROPE
- **note**: SG OPTION EUROPE - SYSTEMATIC INTERNALISER BUSINESSES.
- **hasFacilityAcronym**: SGOE SI
- **hasFormalName**: SG OPTION EUROPE
- **hasWebsite**: http://www.sgcib.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
