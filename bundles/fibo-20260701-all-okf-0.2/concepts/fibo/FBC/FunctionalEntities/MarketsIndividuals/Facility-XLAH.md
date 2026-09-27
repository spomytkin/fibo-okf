---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: LAHORE STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: LAHORE STOCK EXCHANGE HAS BEEN INTEGRATED TO THE PAKISTAN STOCK EXCHANGE IN JANUARY 2017.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: LSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: LAHORE STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.lahorestock.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Lahore.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Lahore
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-LAHORESTOCKEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-LAHORESTOCKEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Pakistan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XLAH
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: LAHORE STOCK EXCHANGE
type: Ontology Individual
---

# LAHORE STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XLAH>

## Relationships

- **Related to**: [Pakistan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Pakistan>)
- **Related to**: [Lahore](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Lahore.md)
- **Related to**: [ServiceProvider-LAHORESTOCKEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-LAHORESTOCKEXCHANGE.md)

## Annotations

- **label**: LAHORE STOCK EXCHANGE
- **note**: LAHORE STOCK EXCHANGE HAS BEEN INTEGRATED TO THE PAKISTAN STOCK EXCHANGE IN JANUARY 2017.
- **hasFacilityAcronym**: LSE
- **hasFormalName**: LAHORE STOCK EXCHANGE
- **hasWebsite**: http://www.lahorestock.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
