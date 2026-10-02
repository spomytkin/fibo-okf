---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: BLUE OCEAN ALTERNATIVE TRADING SYSTEM
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: 'BLUE OCEAN ATS, LLC IS A US REGISTERED BROKER DEALER (CRD #306512) AND OPERATOR OF AN ALTERNATIVE TRADING SYSTEM
      (ATS).'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: BOATS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: BLUE OCEAN ALTERNATIVE TRADING SYSTEM
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.blueoceanats.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sea_Girt.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Sea_Girt
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BLUEOCEANATSLLC.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BLUEOCEANATSLLC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OCEA
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: BLUE OCEAN ALTERNATIVE TRADING SYSTEM
type: Ontology Individual
---

# BLUE OCEAN ALTERNATIVE TRADING SYSTEM

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OCEA>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Sea_Girt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Sea_Girt.md)
- **Related to**: [ServiceProvider-BLUEOCEANATSLLC](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-BLUEOCEANATSLLC.md)

## Annotations

- **label**: BLUE OCEAN ALTERNATIVE TRADING SYSTEM
- **note**: BLUE OCEAN ATS, LLC IS A US REGISTERED BROKER DEALER (CRD #306512) AND OPERATOR OF AN ALTERNATIVE TRADING SYSTEM (ATS).
- **hasFacilityAcronym**: BOATS
- **hasFormalName**: BLUE OCEAN ALTERNATIVE TRADING SYSTEM
- **hasWebsite**: http://www.blueoceanats.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
