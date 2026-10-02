---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BSE SME
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: BSE SME PLATFORM.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BSE SME
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BSE SME
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.bseindia.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MultilateralTradingFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Mumbai.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Mumbai
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBOM.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBOM
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-335800UOTLCPTZQVDA19.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-335800UOTLCPTZQVDA19
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/India
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BSME
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BSE SME
type: Ontology Individual
---

# BSE SME

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-BSME>

## Relationships

- **Related to**: [India](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/India>)
- **Related to**: [Mumbai](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Mumbai.md)
- **Related to**: [Facility-XBOM](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XBOM.md)
- **Related to**: [ServiceProvider-L-335800UOTLCPTZQVDA19](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-335800UOTLCPTZQVDA19.md)

## Annotations

- **label**: BSE SME
- **note**: BSE SME PLATFORM.
- **hasFacilityAcronym**: BSE SME
- **hasFormalName**: BSE SME
- **hasWebsite**: http://www.bseindia.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
