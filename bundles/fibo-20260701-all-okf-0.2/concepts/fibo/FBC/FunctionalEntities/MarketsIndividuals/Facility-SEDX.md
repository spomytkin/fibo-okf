---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SECURITISED DERIVATIVES MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MULTILATERAL TRADING FACILITY.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SEDEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SECURITISED DERIVATIVES MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.borsaitaliana.it
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Milan.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Milan
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMIL.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMIL
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-8156005391EE905D3124.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-8156005391EE905D3124
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Italy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SEDX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SECURITISED DERIVATIVES MARKET
type: Ontology Individual
---

# SECURITISED DERIVATIVES MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-SEDX>

## Relationships

- **Related to**: [Italy](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Italy>)
- **Related to**: [Milan](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Milan.md)
- **Related to**: [Facility-XMIL](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMIL.md)
- **Related to**: [ServiceProvider-L-8156005391EE905D3124](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-8156005391EE905D3124.md)

## Annotations

- **label**: SECURITISED DERIVATIVES MARKET
- **note**: MULTILATERAL TRADING FACILITY.
- **hasFacilityAcronym**: SEDEX
- **hasFormalName**: SECURITISED DERIVATIVES MARKET
- **hasWebsite**: http://www.borsaitaliana.it

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
