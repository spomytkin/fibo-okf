---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: INDONESIA STOCK EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: THE JAKARTA (JSX) AND SURABAYA (SSX) STOCK EXCHANGES HAVE MERGED TO BECOME THE INDONESIA STOCK EXCHANGE (IDX).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: IDX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: INDONESIA STOCK EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.idx.co.id
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jakarta.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Jakarta
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-INDONESIASTOCKEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-INDONESIASTOCKEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Indonesia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XIDX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: INDONESIA STOCK EXCHANGE
type: Ontology Individual
---

# INDONESIA STOCK EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XIDX>

## Relationships

- **Related to**: [Indonesia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Indonesia>)
- **Related to**: [Jakarta](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jakarta.md)
- **Related to**: [ServiceProvider-INDONESIASTOCKEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-INDONESIASTOCKEXCHANGE.md)

## Annotations

- **label**: INDONESIA STOCK EXCHANGE
- **note**: THE JAKARTA (JSX) AND SURABAYA (SSX) STOCK EXCHANGES HAVE MERGED TO BECOME THE INDONESIA STOCK EXCHANGE (IDX).
- **hasFacilityAcronym**: IDX
- **hasFormalName**: INDONESIA STOCK EXCHANGE
- **hasWebsite**: http://www.idx.co.id

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
