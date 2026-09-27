---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SYDNEY STOCK EXCHANGE LIMITED
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: AS A SECURITIES EXCHANGE,SSX PROVIDES LISTING FACILITIES TO COMPANIES AND SECURITIES ISSUERS AS WELL AS TRADING
      FACILITIES FOR STOCK BROKERS, TRADERS AND INVESTORS TO BUY AND SELL SHARES/SECURITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SSX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SYDNEY STOCK EXCHANGE LIMITED
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.ssx.sydney
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SYDNEYSTOCKEXCHANGELIMITED.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SYDNEYSTOCKEXCHANGELIMITED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-APXL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SYDNEY STOCK EXCHANGE LIMITED
type: Ontology Individual
---

# SYDNEY STOCK EXCHANGE LIMITED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-APXL>

## Relationships

- **Related to**: [Australia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia>)
- **Related to**: [Sydney](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney.md)
- **Related to**: [ServiceProvider-SYDNEYSTOCKEXCHANGELIMITED](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SYDNEYSTOCKEXCHANGELIMITED.md)

## Annotations

- **label**: SYDNEY STOCK EXCHANGE LIMITED
- **note**: AS A SECURITIES EXCHANGE,SSX PROVIDES LISTING FACILITIES TO COMPANIES AND SECURITIES ISSUERS AS WELL AS TRADING FACILITIES FOR STOCK BROKERS, TRADERS AND INVESTORS TO BUY AND SELL SHARES/SECURITIES.
- **hasFacilityAcronym**: SSX
- **hasFormalName**: SYDNEY STOCK EXCHANGE LIMITED
- **hasWebsite**: http://www.ssx.sydney

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
