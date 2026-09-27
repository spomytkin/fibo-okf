---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MTS SWAP MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: B2C SEGMENT OF EUROMTS LTD.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: STF
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MTS SWAP MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.mtsmarkets.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/London
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMTS.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMTS
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MTSSWAPMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MTSSWAPMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MTSW
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MTS SWAP MARKET
type: Ontology Individual
---

# MTS SWAP MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-MTSW>

## Relationships

- **Related to**: [UnitedKingdomOfGreatBritainAndNorthernIreland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland>)
- **Related to**: [London](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md)
- **Related to**: [Facility-XMTS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMTS.md)
- **Related to**: [ServiceProvider-MTSSWAPMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-MTSSWAPMARKET.md)

## Annotations

- **label**: MTS SWAP MARKET
- **note**: B2C SEGMENT OF EUROMTS LTD.
- **hasFacilityAcronym**: STF
- **hasFormalName**: MTS SWAP MARKET
- **hasWebsite**: http://www.mtsmarkets.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
