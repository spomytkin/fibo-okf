---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EMS EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED MARKET FOR SECURITIES, ELECTRONIC TRADING PLATFORM.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: EMS EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.vanlanschot.nl
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/S-hertogenbosch.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/S-hertogenbosch
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-724500ZM85SCL0RS8L71.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-724500ZM85SCL0RS8L71
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEMS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: EMS EXCHANGE
type: Ontology Individual
---

# EMS EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEMS>

## Relationships

- **Related to**: [Netherlands](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Netherlands>)
- **Related to**: [S-hertogenbosch](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/S-hertogenbosch.md)
- **Related to**: [ServiceProvider-L-724500ZM85SCL0RS8L71](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-724500ZM85SCL0RS8L71.md)

## Annotations

- **label**: EMS EXCHANGE
- **note**: REGISTERED MARKET FOR SECURITIES, ELECTRONIC TRADING PLATFORM.
- **hasFormalName**: EMS EXCHANGE
- **hasWebsite**: http://www.vanlanschot.nl

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
