---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: GASPOINT NORDIC A/S
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: GASPOINT NORDIC IS OPERATING A PLATFORM FOR CONTINUOUS ELECTRONIC TRADING OF GAS, DELIVERABLE TO THE ETF VIRTUAL
      TRADING POINT.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: GPN
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: GASPOINT NORDIC A/S
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.gaspointnordic.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Copenhagen.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Copenhagen
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-GASPOINTNORDICAS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-GASPOINTNORDICAS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Denmark
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NPGA
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: GASPOINT NORDIC A/S
type: Ontology Individual
---

# GASPOINT NORDIC A/S

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NPGA>

## Relationships

- **Related to**: [Denmark](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Denmark>)
- **Related to**: [Copenhagen](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Copenhagen.md)
- **Related to**: [ServiceProvider-GASPOINTNORDICAS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-GASPOINTNORDICAS.md)

## Annotations

- **label**: GASPOINT NORDIC A/S
- **note**: GASPOINT NORDIC IS OPERATING A PLATFORM FOR CONTINUOUS ELECTRONIC TRADING OF GAS, DELIVERABLE TO THE ETF VIRTUAL TRADING POINT.
- **hasFacilityAcronym**: GPN
- **hasFormalName**: GASPOINT NORDIC A/S
- **hasWebsite**: http://www.gaspointnordic.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
