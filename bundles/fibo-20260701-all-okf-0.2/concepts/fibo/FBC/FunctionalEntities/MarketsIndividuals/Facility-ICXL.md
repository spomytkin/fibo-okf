---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: INDIAN COMMODITY EXCHANGE LTD
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: INDIAN COMMODITY EXCHANGE LTD IS A SCREEN BASED ON-LINE DERIVATIVES EXCHANGE FOR COMMODITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ICEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: INDIAN COMMODITY EXCHANGE LTD
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.icexindia.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Mumbai.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Mumbai
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-INDIANCOMMODITYEXCHANGELTD.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-INDIANCOMMODITYEXCHANGELTD
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/India
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ICXL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: INDIAN COMMODITY EXCHANGE LTD
type: Ontology Individual
---

# INDIAN COMMODITY EXCHANGE LTD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ICXL>

## Relationships

- **Related to**: [India](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/India>)
- **Related to**: [Mumbai](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Mumbai.md)
- **Related to**: [ServiceProvider-INDIANCOMMODITYEXCHANGELTD](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-INDIANCOMMODITYEXCHANGELTD.md)

## Annotations

- **label**: INDIAN COMMODITY EXCHANGE LTD
- **note**: INDIAN COMMODITY EXCHANGE LTD IS A SCREEN BASED ON-LINE DERIVATIVES EXCHANGE FOR COMMODITIES.
- **hasFacilityAcronym**: ICEX
- **hasFormalName**: INDIAN COMMODITY EXCHANGE LTD
- **hasWebsite**: http://www.icexindia.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
