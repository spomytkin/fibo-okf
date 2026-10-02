---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: RIVERCROSS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: RIVERCROSS IS AN ALTERNATIVE TRADING SYSTEM (ATS) OPERATED PURSUANT TO REGULATION ATS BY RIVERCROSS SECURITIES,
      LLLP, PROVIDING A SECURE AND CONFIDENTIAL LIQUIDITY SOURCE FOR U.S.-REGISTERED BROKER-DEALERS AND THEIR CLIENTS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: RIVERCROSS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.rxats.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Narberth.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Narberth
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-RIVERCROSSSECURITESLP.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-RIVERCROSSSECURITESLP
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-RICX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: RIVERCROSS
type: Ontology Individual
---

# RIVERCROSS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-RICX>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Narberth](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Narberth.md)
- **Related to**: [ServiceProvider-RIVERCROSSSECURITESLP](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-RIVERCROSSSECURITESLP.md)

## Annotations

- **label**: RIVERCROSS
- **note**: RIVERCROSS IS AN ALTERNATIVE TRADING SYSTEM (ATS) OPERATED PURSUANT TO REGULATION ATS BY RIVERCROSS SECURITIES, LLLP, PROVIDING A SECURE AND CONFIDENTIAL LIQUIDITY SOURCE FOR U.S.-REGISTERED BROKER-DEALERS AND THEIR CLIENTS.
- **hasFormalName**: RIVERCROSS
- **hasWebsite**: http://www.rxats.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
