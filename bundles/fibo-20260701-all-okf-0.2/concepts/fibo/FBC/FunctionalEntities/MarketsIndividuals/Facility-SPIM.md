---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ST. PETERSBURG INTERNATIONAL MERCANTILE EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERD COMMODITIES MARKET - OIL.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SPIMEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: ST. PETERSBURG INTERNATIONAL MERCANTILE EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.s-pimex.ru
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Petersburg.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Petersburg
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STPETERSBURGINTERNATIONALMERCANTILEEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STPETERSBURGINTERNATIONALMERCANTILEEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SPIM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: ST. PETERSBURG INTERNATIONAL MERCANTILE EXCHANGE
type: Ontology Individual
---

# ST. PETERSBURG INTERNATIONAL MERCANTILE EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SPIM>

## Relationships

- **Related to**: [RussianFederation](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation>)
- **Related to**: [Saint_Petersburg](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Petersburg.md)
- **Related to**: [ServiceProvider-STPETERSBURGINTERNATIONALMERCANTILEEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-STPETERSBURGINTERNATIONALMERCANTILEEXCHANGE.md)

## Annotations

- **label**: ST. PETERSBURG INTERNATIONAL MERCANTILE EXCHANGE
- **note**: REGISTERD COMMODITIES MARKET - OIL.
- **hasFacilityAcronym**: SPIMEX
- **hasFormalName**: ST. PETERSBURG INTERNATIONAL MERCANTILE EXCHANGE
- **hasWebsite**: http://www.s-pimex.ru

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
