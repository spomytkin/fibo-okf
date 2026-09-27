---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SHANGHAI STOCK EXCHANGE - SHANGHAI - HONG KONG STOCK CONNECT
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: FOREIGN INVESTORS TRADING IN A-SHARE STOCK LISTED IN SHANGHAI STOCK EXCHANGE UNDER SHANGHAI-HONG KONG STOCK CONNECT
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SHANGHAI STOCK EXCHANGE - SHANGHAI - HONG KONG STOCK CONNECT
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.sse.com.cn
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Shanghai.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Shanghai
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSHG.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSHG
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-300300LRJ5FEZ23N8725.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-300300LRJ5FEZ23N8725
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/China
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSSC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SHANGHAI STOCK EXCHANGE - SHANGHAI - HONG KONG STOCK CONNECT
type: Ontology Individual
---

# SHANGHAI STOCK EXCHANGE - SHANGHAI - HONG KONG STOCK CONNECT

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSSC>

## Relationships

- **Related to**: [China](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/China>)
- **Related to**: [Shanghai](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Shanghai.md)
- **Related to**: [Facility-XSHG](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSHG.md)
- **Related to**: [ServiceProvider-L-300300LRJ5FEZ23N8725](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-300300LRJ5FEZ23N8725.md)

## Annotations

- **label**: SHANGHAI STOCK EXCHANGE - SHANGHAI - HONG KONG STOCK CONNECT
- **note**: FOREIGN INVESTORS TRADING IN A-SHARE STOCK LISTED IN SHANGHAI STOCK EXCHANGE UNDER SHANGHAI-HONG KONG STOCK CONNECT
- **hasFacilityAcronym**: SSE
- **hasFormalName**: SHANGHAI STOCK EXCHANGE - SHANGHAI - HONG KONG STOCK CONNECT
- **hasWebsite**: http://www.sse.com.cn

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
