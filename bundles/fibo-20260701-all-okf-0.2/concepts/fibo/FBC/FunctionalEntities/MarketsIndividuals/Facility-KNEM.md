---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: KNIGHT EQUITY MARKETS LP
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: KEM OPERATES AS A MARKET-MAKER IN OVER-THE-COUNTER EQUITY SECURITIES, PRIMARILY THOSE TRADED IN THE NASDAQ STOCK
      MARKET AND ON THE OTC BULLETIN BOARD.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: KNIGHT EQUITY MARKETS LP
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.knight.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-KNIG.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-KNIG
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KNIGHTEQUITYMARKETSLP.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KNIGHTEQUITYMARKETSLP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-KNEM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: KNIGHT EQUITY MARKETS LP
type: Ontology Individual
---

# KNIGHT EQUITY MARKETS LP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-KNEM>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Jersey_City](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City.md)
- **Related to**: [Facility-KNIG](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-KNIG.md)
- **Related to**: [ServiceProvider-KNIGHTEQUITYMARKETSLP](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-KNIGHTEQUITYMARKETSLP.md)

## Annotations

- **label**: KNIGHT EQUITY MARKETS LP
- **note**: KEM OPERATES AS A MARKET-MAKER IN OVER-THE-COUNTER EQUITY SECURITIES, PRIMARILY THOSE TRADED IN THE NASDAQ STOCK MARKET AND ON THE OTC BULLETIN BOARD.
- **hasFormalName**: KNIGHT EQUITY MARKETS LP
- **hasWebsite**: http://www.knight.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
