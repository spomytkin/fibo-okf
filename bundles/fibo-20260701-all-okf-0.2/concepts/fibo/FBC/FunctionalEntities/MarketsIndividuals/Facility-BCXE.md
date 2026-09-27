---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: CBOE EUROPE EQUITIES
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: PAN-EUROPEAN RECOGNISED INVESTMENT EXCHANGE.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: CBOE  EUROPE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: CBOE EUROPE EQUITIES
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.markets.cboe.com/europe/equities/overview/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/London
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900ERRPSKE7UZH711.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900ERRPSKE7UZH711
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BCXE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: CBOE EUROPE EQUITIES
type: Ontology Individual
---

# CBOE EUROPE EQUITIES

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BCXE>

## Relationships

- **Related to**: [UnitedKingdomOfGreatBritainAndNorthernIreland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland>)
- **Related to**: [London](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md)
- **Related to**: [ServiceProvider-L-254900ERRPSKE7UZH711](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900ERRPSKE7UZH711.md)

## Annotations

- **label**: CBOE EUROPE EQUITIES
- **note**: PAN-EUROPEAN RECOGNISED INVESTMENT EXCHANGE.
- **hasFacilityAcronym**: CBOE  EUROPE
- **hasFormalName**: CBOE EUROPE EQUITIES
- **hasWebsite**: http://www.markets.cboe.com/europe/equities/overview/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
