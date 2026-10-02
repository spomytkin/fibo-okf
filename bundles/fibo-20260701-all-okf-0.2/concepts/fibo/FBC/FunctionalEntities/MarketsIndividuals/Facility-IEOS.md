---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: IBKR EOS ATS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: IEOS IS AN ALTERNATIVE TRADING SYSTEM OPERATED PURSUANT TO REGULATION ATS BY INTERACTIVE BROKERS LLC.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: IEOS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: IBKR EOS ATS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.interactivebrokers.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/AlternativeTradingSystem
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Greenwich.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Greenwich
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBKR.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBKR
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-50OBSE5T5521O6SMZR28.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-50OBSE5T5521O6SMZR28
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IEOS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: IBKR EOS ATS
type: Ontology Individual
---

# IBKR EOS ATS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-IEOS>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Greenwich](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Greenwich.md)
- **Related to**: [Facility-IBKR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-IBKR.md)
- **Related to**: [ServiceProvider-L-50OBSE5T5521O6SMZR28](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-50OBSE5T5521O6SMZR28.md)

## Annotations

- **label**: IBKR EOS ATS
- **note**: IEOS IS AN ALTERNATIVE TRADING SYSTEM OPERATED PURSUANT TO REGULATION ATS BY INTERACTIVE BROKERS LLC.
- **hasFacilityAcronym**: IEOS
- **hasFormalName**: IBKR EOS ATS
- **hasWebsite**: http://www.interactivebrokers.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
