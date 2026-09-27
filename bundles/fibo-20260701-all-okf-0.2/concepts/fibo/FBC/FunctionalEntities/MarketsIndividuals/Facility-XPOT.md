---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EUROPEAN ENERGY EXCHANGE - OTF GAS MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: OTF SEGMENT OF THE EEX GAS MARKETS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: EEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: EUROPEAN ENERGY EXCHANGE - OTF GAS MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.eex.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OrganizedTradingFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Leipzig.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Leipzig
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEEE.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEEE
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900J0JGLSFDWNFC20.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900J0JGLSFDWNFC20
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPOT
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: EUROPEAN ENERGY EXCHANGE - OTF GAS MARKET
type: Ontology Individual
---

# EUROPEAN ENERGY EXCHANGE - OTF GAS MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPOT>

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Leipzig](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Leipzig.md)
- **Related to**: [Facility-XEEE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XEEE.md)
- **Related to**: [ServiceProvider-L-529900J0JGLSFDWNFC20](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-529900J0JGLSFDWNFC20.md)

## Annotations

- **label**: EUROPEAN ENERGY EXCHANGE - OTF GAS MARKET
- **note**: OTF SEGMENT OF THE EEX GAS MARKETS.
- **hasFacilityAcronym**: EEX
- **hasFormalName**: EUROPEAN ENERGY EXCHANGE - OTF GAS MARKET
- **hasWebsite**: http://www.eex.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
