---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NASDAQ ICELAND HF. - NORDIC@MID
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: NORDIC@MID DARK POOL FOR XICE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: ICEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NASDAQ ICELAND HF. - NORDIC@MID
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nasdaqomxnordic.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Reykjavik.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Reykjavik
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XICE.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XICE
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5493000SYSCC8J8U5638.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5493000SYSCC8J8U5638
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Iceland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DICE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NASDAQ ICELAND HF. - NORDIC@MID
type: Ontology Individual
---

# NASDAQ ICELAND HF. - NORDIC@MID

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DICE>

## Relationships

- **Related to**: [Iceland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Iceland>)
- **Related to**: [Reykjavik](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Reykjavik.md)
- **Related to**: [Facility-XICE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XICE.md)
- **Related to**: [ServiceProvider-L-5493000SYSCC8J8U5638](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5493000SYSCC8J8U5638.md)

## Annotations

- **label**: NASDAQ ICELAND HF. - NORDIC@MID
- **note**: NORDIC@MID DARK POOL FOR XICE
- **hasFacilityAcronym**: ICEX
- **hasFormalName**: NASDAQ ICELAND HF. - NORDIC@MID
- **hasWebsite**: http://www.nasdaqomxnordic.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
