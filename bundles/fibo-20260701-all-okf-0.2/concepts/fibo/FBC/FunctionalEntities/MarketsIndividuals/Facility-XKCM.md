---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: KOREA EXCHANGE COMMODITY MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: REGISTERED MARKET FOR COMMODITY SUCH AS GOLD, PETRO, ETC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: KOREA EXCHANGE COMMODITY MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://kcm.krx.co.kr
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Seoul.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Seoul
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKRX.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKRX
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KOREAEXCHANGECOMMODITYMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KOREAEXCHANGECOMMODITYMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/KoreaRepublicOf
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKCM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: KOREA EXCHANGE COMMODITY MARKET
type: Ontology Individual
---

# KOREA EXCHANGE COMMODITY MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKCM>

## Relationships

- **Related to**: [KoreaRepublicOf](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/KoreaRepublicOf>)
- **Related to**: [Seoul](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Seoul.md)
- **Related to**: [Facility-XKRX](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKRX.md)
- **Related to**: [ServiceProvider-KOREAEXCHANGECOMMODITYMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KOREAEXCHANGECOMMODITYMARKET.md)

## Annotations

- **label**: KOREA EXCHANGE COMMODITY MARKET
- **note**: REGISTERED MARKET FOR COMMODITY SUCH AS GOLD, PETRO, ETC
- **hasFormalName**: KOREA EXCHANGE COMMODITY MARKET
- **hasWebsite**: http://kcm.krx.co.kr

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
