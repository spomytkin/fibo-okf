---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ASIA PACIFIC CLEAR
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: APEX'S CLEARING HOUSE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: APEX CLEAR
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: ASIA PACIFIC CLEAR
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.asiapacificex.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-APEX.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-APEX
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ASIAPACIFICCLEAR.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ASIAPACIFICCLEAR
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Singapore
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-APCL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: ASIA PACIFIC CLEAR
type: Ontology Individual
---

# ASIA PACIFIC CLEAR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-APCL>

## Relationships

- **Related to**: [Singapore](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Singapore>)
- **Related to**: [Singapore](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore.md)
- **Related to**: [Facility-APEX](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-APEX.md)
- **Related to**: [ServiceProvider-ASIAPACIFICCLEAR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-ASIAPACIFICCLEAR.md)

## Annotations

- **label**: ASIA PACIFIC CLEAR
- **note**: APEX'S CLEARING HOUSE.
- **hasFacilityAcronym**: APEX CLEAR
- **hasFormalName**: ASIA PACIFIC CLEAR
- **hasWebsite**: http://www.asiapacificex.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
