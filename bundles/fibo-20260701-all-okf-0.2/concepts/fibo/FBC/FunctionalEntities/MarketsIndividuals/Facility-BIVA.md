---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BOLSA INSTITUCIONAL DE VALORES
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: STOCK EXCHANGE.LIVE IN Q1 2018.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BIVA
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BOLSA INSTITUCIONAL DE VALORES
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.biva.mx
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Mexico_City.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Mexico_City
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-894500CS2D6RLGW61A19.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-894500CS2D6RLGW61A19
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mexico
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BIVA
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BOLSA INSTITUCIONAL DE VALORES
type: Ontology Individual
---

# BOLSA INSTITUCIONAL DE VALORES

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BIVA>

## Relationships

- **Related to**: [Mexico](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mexico>)
- **Related to**: [Mexico_City](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Mexico_City.md)
- **Related to**: [ServiceProvider-L-894500CS2D6RLGW61A19](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-894500CS2D6RLGW61A19.md)

## Annotations

- **label**: BOLSA INSTITUCIONAL DE VALORES
- **note**: STOCK EXCHANGE.LIVE IN Q1 2018.
- **hasFacilityAcronym**: BIVA
- **hasFormalName**: BOLSA INSTITUCIONAL DE VALORES
- **hasWebsite**: http://www.biva.mx

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
