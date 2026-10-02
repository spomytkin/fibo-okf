---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ASX - PUREMATCH
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: ASX PUREMATCH IS AN ADDITIONAL ORDER BOOK LAUNCHING IN MID 2011 AIMED AT MEETING THE NEEDS OF LATENCY SENSITIVE
      TRADERS, PROVIDING TRADING IN A SUBSET OF ASX LISTED SECURITIES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ASX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: ASX - PUREMATCH
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.asx.com.au/trading_services/asx-trade.htm
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XASX.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XASX
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300USWUR0S7VMM868.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300USWUR0S7VMM868
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ASXP
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: ASX - PUREMATCH
type: Ontology Individual
---

# ASX - PUREMATCH

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-ASXP>

## Relationships

- **Related to**: [Australia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Australia>)
- **Related to**: [Sydney](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sydney.md)
- **Related to**: [Facility-XASX](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XASX.md)
- **Related to**: [ServiceProvider-L-549300USWUR0S7VMM868](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300USWUR0S7VMM868.md)

## Annotations

- **label**: ASX - PUREMATCH
- **note**: ASX PUREMATCH IS AN ADDITIONAL ORDER BOOK LAUNCHING IN MID 2011 AIMED AT MEETING THE NEEDS OF LATENCY SENSITIVE TRADERS, PROVIDING TRADING IN A SUBSET OF ASX LISTED SECURITIES.
- **hasFacilityAcronym**: ASX
- **hasFormalName**: ASX - PUREMATCH
- **hasWebsite**: http://www.asx.com.au/trading_services/asx-trade.htm

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
