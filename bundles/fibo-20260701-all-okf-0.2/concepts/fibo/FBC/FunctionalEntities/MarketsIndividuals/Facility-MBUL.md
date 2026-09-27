---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MTF SOFIA
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MULTILATERAL TRADING FACILITY FOR EQUITIES, BONDS, DERIVATIVES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MTF SOFIA
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.capman.bg
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sofia.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Sofia
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5299003795MPR9UZ1J25.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5299003795MPR9UZ1J25
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Bulgaria
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MBUL
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MTF SOFIA
type: Ontology Individual
---

# MTF SOFIA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MBUL>

## Relationships

- **Related to**: [Bulgaria](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Bulgaria>)
- **Related to**: [Sofia](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sofia.md)
- **Related to**: [ServiceProvider-L-5299003795MPR9UZ1J25](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5299003795MPR9UZ1J25.md)

## Annotations

- **label**: MTF SOFIA
- **note**: MULTILATERAL TRADING FACILITY FOR EQUITIES, BONDS, DERIVATIVES.
- **hasFormalName**: MTF SOFIA
- **hasWebsite**: http://www.capman.bg

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
