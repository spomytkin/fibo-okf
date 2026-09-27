---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CHI-EAST
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: EXCHANGE-BACKED NON DISPLAY VENUE IN ASIA, FOR SECURITIES LISTED IN AUSTRALIA, HONG KONG, JAPAN AND SINGAPORE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: CHI-EAST
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.chi-east.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CHI-EAST.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CHI-EAST
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Singapore
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: CHI-EAST
type: Ontology Individual
---

# CHI-EAST

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-CHIE>

## Relationships

- **Related to**: [Singapore](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Singapore>)
- **Related to**: [Singapore](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Singapore.md)
- **Related to**: [ServiceProvider-CHI-EAST](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-CHI-EAST.md)

## Annotations

- **label**: CHI-EAST
- **note**: EXCHANGE-BACKED NON DISPLAY VENUE IN ASIA, FOR SECURITIES LISTED IN AUSTRALIA, HONG KONG, JAPAN AND SINGAPORE.
- **hasFormalName**: CHI-EAST
- **hasWebsite**: http://www.chi-east.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
