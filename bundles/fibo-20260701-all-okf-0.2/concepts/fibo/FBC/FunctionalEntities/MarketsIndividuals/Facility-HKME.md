---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: HONG KONG MERCANTILE EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: HKMEX HAS CEASED ITS ACTIVITIES IN MAY 2013.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: HKMEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: HONG KONG MERCANTILE EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.hkmerc.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Hong_Kong.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Hong_Kong
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800YTVSXYQN17BW16.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800YTVSXYQN17BW16
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/HongKong
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-HKME
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: HONG KONG MERCANTILE EXCHANGE
type: Ontology Individual
---

# HONG KONG MERCANTILE EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-HKME>

## Relationships

- **Related to**: [HongKong](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/HongKong>)
- **Related to**: [Hong_Kong](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Hong_Kong.md)
- **Related to**: [ServiceProvider-L-213800YTVSXYQN17BW16](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-213800YTVSXYQN17BW16.md)

## Annotations

- **label**: HONG KONG MERCANTILE EXCHANGE
- **note**: HKMEX HAS CEASED ITS ACTIVITIES IN MAY 2013.
- **hasFacilityAcronym**: HKMEX
- **hasFormalName**: HONG KONG MERCANTILE EXCHANGE
- **hasWebsite**: http://www.hkmerc.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
