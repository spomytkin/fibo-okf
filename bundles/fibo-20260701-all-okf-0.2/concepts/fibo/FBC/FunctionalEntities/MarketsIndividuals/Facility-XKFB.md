---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: KOREA FREEBOARD MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: FREEBOARD IS A NEW MARKET FOR COMPANIES LISTED, NEITHER ON THE STOCK MARKET DIVISION NOR ON THE KOSDAQ MARKET DIVISION
      OF KRX.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: KOREA FREEBOARD MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.ksda.or.kr/english/invest/otc_overview.cfm
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Seoul.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Seoul
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KOREAFREEBOARDMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KOREAFREEBOARDMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/KoreaRepublicOf
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKFB
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: KOREA FREEBOARD MARKET
type: Ontology Individual
---

# KOREA FREEBOARD MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XKFB>

## Relationships

- **Related to**: [KoreaRepublicOf](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/KoreaRepublicOf>)
- **Related to**: [Seoul](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Seoul.md)
- **Related to**: [ServiceProvider-KOREAFREEBOARDMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KOREAFREEBOARDMARKET.md)

## Annotations

- **label**: KOREA FREEBOARD MARKET
- **note**: FREEBOARD IS A NEW MARKET FOR COMPANIES LISTED, NEITHER ON THE STOCK MARKET DIVISION NOR ON THE KOSDAQ MARKET DIVISION OF KRX.
- **hasFormalName**: KOREA FREEBOARD MARKET
- **hasWebsite**: http://www.ksda.or.kr/english/invest/otc_overview.cfm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
