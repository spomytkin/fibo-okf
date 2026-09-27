---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: TRADEWEB FX OPTIONS
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MULTIDEALER- TO-CUSTOMER TRADING PLATFORM FOR FX OPTIONS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: TRADEWEB FX OPTIONS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.tradeweb.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-TRWB.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-TRWB
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-TRADEWEBFXOPTIONS.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-TRADEWEBFXOPTIONS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-TRFX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: TRADEWEB FX OPTIONS
type: Ontology Individual
---

# TRADEWEB FX OPTIONS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-TRFX>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Jersey_City](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City.md)
- **Related to**: [Facility-TRWB](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-TRWB.md)
- **Related to**: [ServiceProvider-TRADEWEBFXOPTIONS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-TRADEWEBFXOPTIONS.md)

## Annotations

- **label**: TRADEWEB FX OPTIONS
- **note**: MULTIDEALER- TO-CUSTOMER TRADING PLATFORM FOR FX OPTIONS.
- **hasFormalName**: TRADEWEB FX OPTIONS
- **hasWebsite**: http://www.tradeweb.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
