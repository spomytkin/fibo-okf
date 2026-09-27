---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BARBADOS STOCK EXCHANGE - JUNIOR MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MARKET FOR SMALL COMPANIES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BSE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BARBADOS STOCK EXCHANGE - JUNIOR MARKET
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
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BARBADOSSTOCKEXCHANGE-JUNIORMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BARBADOSSTOCKEXCHANGE-JUNIORMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Barbados
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BAJM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BARBADOS STOCK EXCHANGE - JUNIOR MARKET
type: Ontology Individual
---

# BARBADOS STOCK EXCHANGE - JUNIOR MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BAJM>

## Relationships

- **Related to**: [Barbados](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Barbados>)
- **Related to**: [Bridgetown](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bridgetown.md)
- **Related to**: [Facility-XBAB](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBAB.md)
- **Related to**: [ServiceProvider-BARBADOSSTOCKEXCHANGE-JUNIORMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BARBADOSSTOCKEXCHANGE-JUNIORMARKET.md)

## Annotations

- **label**: BARBADOS STOCK EXCHANGE - JUNIOR MARKET
- **note**: MARKET FOR SMALL COMPANIES
- **hasFacilityAcronym**: BSE
- **hasFormalName**: BARBADOS STOCK EXCHANGE - JUNIOR MARKET
- **hasWebsite**: http://www.bse.com.bb

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
