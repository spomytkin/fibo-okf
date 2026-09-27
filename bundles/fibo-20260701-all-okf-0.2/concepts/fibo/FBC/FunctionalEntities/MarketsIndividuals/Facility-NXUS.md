---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NX ATS - CROSSING PLATFORM
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: NX IS A REGISTERED ATS IN THE US MARKETS - CURRENTLY PROVIDING CROSSING FACILITIES FOR REG NMS LISTED STOCKS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NX ATS - CROSSING PLATFORM
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nomura.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NXATS-CROSSINGPLATFORM.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NXATS-CROSSINGPLATFORM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NXUS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NX ATS - CROSSING PLATFORM
type: Ontology Individual
---

# NX ATS - CROSSING PLATFORM

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NXUS>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [ServiceProvider-NXATS-CROSSINGPLATFORM](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-NXATS-CROSSINGPLATFORM.md)

## Annotations

- **label**: NX ATS - CROSSING PLATFORM
- **note**: NX IS A REGISTERED ATS IN THE US MARKETS - CURRENTLY PROVIDING CROSSING FACILITIES FOR REG NMS LISTED STOCKS.
- **hasFormalName**: NX ATS - CROSSING PLATFORM
- **hasWebsite**: http://www.nomura.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
