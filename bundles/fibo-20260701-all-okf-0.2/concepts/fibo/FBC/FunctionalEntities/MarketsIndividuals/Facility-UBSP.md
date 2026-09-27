---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: UBS PIN (UBS PRICE IMPROVEMENT NETWORK)
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: UBS PRICE IMPROVEMENT NETWORK IN THE US (EQUITIES).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: UBS PIN (UBS PRICE IMPROVEMENT NETWORK)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.ubs.com/ats
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-UBSA.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-UBSA
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-UBSPINUBSPRICEIMPROVEMENTNETWORK.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-UBSPINUBSPRICEIMPROVEMENTNETWORK
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-UBSP
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: UBS PIN (UBS PRICE IMPROVEMENT NETWORK)
type: Ontology Individual
---

# UBS PIN (UBS PRICE IMPROVEMENT NETWORK)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-UBSP>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [Facility-UBSA](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-UBSA.md)
- **Related to**: [ServiceProvider-UBSPINUBSPRICEIMPROVEMENTNETWORK](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-UBSPINUBSPRICEIMPROVEMENTNETWORK.md)

## Annotations

- **label**: UBS PIN (UBS PRICE IMPROVEMENT NETWORK)
- **note**: UBS PRICE IMPROVEMENT NETWORK IN THE US (EQUITIES).
- **hasFormalName**: UBS PIN (UBS PRICE IMPROVEMENT NETWORK)
- **hasWebsite**: http://www.ubs.com/ats

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
