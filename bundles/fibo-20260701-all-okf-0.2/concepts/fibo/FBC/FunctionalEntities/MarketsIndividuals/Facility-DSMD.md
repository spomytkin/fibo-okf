---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: QATAR STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: DOHA SECURITIES MARKET CHANGED TO QATAR EXCHANGE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: DSM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: QATAR STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.qatarexchange.qa
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Doha.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Doha
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2763V8R4FCPY9DF45J22.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2763V8R4FCPY9DF45J22
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Qatar
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DSMD
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: QATAR STOCK EXCHANGE
type: Ontology Individual
---

# QATAR STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DSMD>

## Relationships

- **Related to**: [Qatar](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Qatar>)
- **Related to**: [Doha](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Doha.md)
- **Related to**: [ServiceProvider-L-2763V8R4FCPY9DF45J22](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-2763V8R4FCPY9DF45J22.md)

## Annotations

- **label**: QATAR STOCK EXCHANGE
- **note**: DOHA SECURITIES MARKET CHANGED TO QATAR EXCHANGE.
- **hasFacilityAcronym**: DSM
- **hasFormalName**: QATAR STOCK EXCHANGE
- **hasWebsite**: http://www.qatarexchange.qa

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
