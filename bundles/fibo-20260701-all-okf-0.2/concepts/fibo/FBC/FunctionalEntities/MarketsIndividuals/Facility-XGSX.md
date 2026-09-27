---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: GLOBAL SECURITIES EXCHANGE
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: EXCHANGE FOR SECURITIES
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: GSX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: GLOBAL SECURITIES EXCHANGE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.gmex-group.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/London
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-GMEG.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GMEG
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-98450080L1F7936CFU76.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-98450080L1F7936CFU76
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XGSX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: GLOBAL SECURITIES EXCHANGE
type: Ontology Individual
---

# GLOBAL SECURITIES EXCHANGE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XGSX>

## Relationships

- **Related to**: [UnitedKingdomOfGreatBritainAndNorthernIreland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland>)
- **Related to**: [London](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md)
- **Related to**: [Facility-GMEG](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-GMEG.md)
- **Related to**: [ServiceProvider-L-98450080L1F7936CFU76](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-98450080L1F7936CFU76.md)

## Annotations

- **label**: GLOBAL SECURITIES EXCHANGE
- **note**: EXCHANGE FOR SECURITIES
- **hasFacilityAcronym**: GSX
- **hasFormalName**: GLOBAL SECURITIES EXCHANGE
- **hasWebsite**: http://www.gmex-group.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
