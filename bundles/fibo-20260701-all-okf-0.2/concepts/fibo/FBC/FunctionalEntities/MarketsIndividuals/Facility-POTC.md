---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: PACIFIC OTC
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: TRADING PLATFORM FOR OTC EQUITIES AND DEBT.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: POTC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: PACIFIC OTC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.pacificotc.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Port_Vila.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Port_Vila
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PACIFICOTC.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PACIFICOTC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Vanuatu
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-POTC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: PACIFIC OTC
type: Ontology Individual
---

# PACIFIC OTC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-POTC>

## Relationships

- **Related to**: [Vanuatu](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Vanuatu>)
- **Related to**: [Port_Vila](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Port_Vila.md)
- **Related to**: [ServiceProvider-PACIFICOTC](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-PACIFICOTC.md)

## Annotations

- **label**: PACIFIC OTC
- **note**: TRADING PLATFORM FOR OTC EQUITIES AND DEBT.
- **hasFacilityAcronym**: POTC
- **hasFormalName**: PACIFIC OTC
- **hasWebsite**: http://www.pacificotc.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
