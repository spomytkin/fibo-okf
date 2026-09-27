---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DUTCH CARIBBEAN SECURITIES EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: INTERNATIONAL EXCHANGE FOR THE LISTING AND TRADING IN DOMESTIC- AND INTERNATIONAL SECURITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: DCSX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: DUTCH CARIBBEAN SECURITIES EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.dcsx.an
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Willemstad.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Willemstad
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DUTCHCARIBBEANSECURITIESEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DUTCHCARIBBEANSECURITIESEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Curacao
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DCSX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: DUTCH CARIBBEAN SECURITIES EXCHANGE
type: Ontology Individual
---

# DUTCH CARIBBEAN SECURITIES EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DCSX>

## Relationships

- **Related to**: [Curacao](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Curacao>)
- **Related to**: [Willemstad](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Willemstad.md)
- **Related to**: [ServiceProvider-DUTCHCARIBBEANSECURITIESEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DUTCHCARIBBEANSECURITIESEXCHANGE.md)

## Annotations

- **label**: DUTCH CARIBBEAN SECURITIES EXCHANGE
- **note**: INTERNATIONAL EXCHANGE FOR THE LISTING AND TRADING IN DOMESTIC- AND INTERNATIONAL SECURITIES.
- **hasFacilityAcronym**: DCSX
- **hasFormalName**: DUTCH CARIBBEAN SECURITIES EXCHANGE
- **hasWebsite**: http://www.dcsx.an

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
