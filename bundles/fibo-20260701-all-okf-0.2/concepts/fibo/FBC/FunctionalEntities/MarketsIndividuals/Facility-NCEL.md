---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: PAKISTAN MERCANTILE EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED FOR LISTED DERIVATIVES (OPTIONS AND FUTURES) TRADING - FORMERLY NATIONAL COMMODITY EXCHANGE LIMITED.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: PMEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: PAKISTAN MERCANTILE EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.pmex.com.pk
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Karachi.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Karachi
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PAKISTANMERCANTILEEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PAKISTANMERCANTILEEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Pakistan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NCEL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: PAKISTAN MERCANTILE EXCHANGE
type: Ontology Individual
---

# PAKISTAN MERCANTILE EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NCEL>

## Relationships

- **Related to**: [Pakistan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Pakistan>)
- **Related to**: [Karachi](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Karachi.md)
- **Related to**: [ServiceProvider-PAKISTANMERCANTILEEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PAKISTANMERCANTILEEXCHANGE.md)

## Annotations

- **label**: PAKISTAN MERCANTILE EXCHANGE
- **note**: REGISTERED FOR LISTED DERIVATIVES (OPTIONS AND FUTURES) TRADING - FORMERLY NATIONAL COMMODITY EXCHANGE LIMITED.
- **hasFacilityAcronym**: PMEX
- **hasFormalName**: PAKISTAN MERCANTILE EXCHANGE
- **hasWebsite**: http://www.pmex.com.pk

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
