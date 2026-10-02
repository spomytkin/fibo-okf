---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BARBADOS STOCK EXCHANGE - INTERNATIONAL SECURITIES MARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ISM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BARBADOS STOCK EXCHANGE - INTERNATIONAL SECURITIES MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bse.com.bb
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bridgetown.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Bridgetown
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBAB.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBAB
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BARBADOSSTOCKEXCHANGE.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BARBADOSSTOCKEXCHANGE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Barbados
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBIS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BARBADOS STOCK EXCHANGE - INTERNATIONAL SECURITIES MARKET
type: Ontology Individual
---

# BARBADOS STOCK EXCHANGE - INTERNATIONAL SECURITIES MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBIS>

## Relationships

- **Related to**: [Barbados](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Barbados>)
- **Related to**: [Bridgetown](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bridgetown.md)
- **Related to**: [Facility-XBAB](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBAB.md)
- **Related to**: [ServiceProvider-BARBADOSSTOCKEXCHANGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BARBADOSSTOCKEXCHANGE.md)

## Annotations

- **label**: BARBADOS STOCK EXCHANGE - INTERNATIONAL SECURITIES MARKET
- **hasFacilityAcronym**: ISM
- **hasFormalName**: BARBADOS STOCK EXCHANGE - INTERNATIONAL SECURITIES MARKET
- **hasWebsite**: http://www.bse.com.bb

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
