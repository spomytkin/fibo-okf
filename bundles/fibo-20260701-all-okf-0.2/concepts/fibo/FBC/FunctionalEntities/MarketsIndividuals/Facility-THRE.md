---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: REFINITIV US SEF LLC
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SWAP EXECUTION FACILITY (SEF).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: RSEF
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: REFINITIV US SEF LLC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.refinitiv.com/en/products/sef-swap-execution-facility
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SwapExecutionFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300WQWDPFSMQ8I087.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300WQWDPFSMQ8I087
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-THRE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: REFINITIV US SEF LLC
type: Ontology Individual
---

# REFINITIV US SEF LLC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-THRE>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [ServiceProvider-L-549300WQWDPFSMQ8I087](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300WQWDPFSMQ8I087.md)

## Annotations

- **label**: REFINITIV US SEF LLC
- **note**: SWAP EXECUTION FACILITY (SEF).
- **hasFacilityAcronym**: RSEF
- **hasFormalName**: REFINITIV US SEF LLC
- **hasWebsite**: http://www.refinitiv.com/en/products/sef-swap-execution-facility

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
