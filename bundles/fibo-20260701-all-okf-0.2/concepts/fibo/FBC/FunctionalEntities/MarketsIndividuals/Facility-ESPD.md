---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NASDAQ OMX ESPEED
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ELECTRONIC FIXED INCOME TRADING PLATFORM.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ESPEED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NASDAQ OMX ESPEED
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nasdaqomx.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NASDAQOMXESPEED.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NASDAQOMXESPEED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ESPD
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NASDAQ OMX ESPEED
type: Ontology Individual
---

# NASDAQ OMX ESPEED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ESPD>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [Facility-XNAS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md)
- **Related to**: [ServiceProvider-NASDAQOMXESPEED](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NASDAQOMXESPEED.md)

## Annotations

- **label**: NASDAQ OMX ESPEED
- **note**: ELECTRONIC FIXED INCOME TRADING PLATFORM.
- **hasFacilityAcronym**: ESPEED
- **hasFormalName**: NASDAQ OMX ESPEED
- **hasWebsite**: http://www.nasdaqomx.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
