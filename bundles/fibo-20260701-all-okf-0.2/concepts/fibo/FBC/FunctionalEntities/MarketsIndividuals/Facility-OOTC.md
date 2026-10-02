---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: OTHER OTC
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: OTC SECURITY THAT IS NOT QUOTED ON THE NNQS (PREVIOUSLY OTCBB) BUT IS ELIGIBLE FOR TRADE REPORTING TO THE TRADE
      REPORTING FACILITY, IS CATEGORIZED AS "OTHER-OTC".
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: OTHER OTC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.otcbb.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/QuoteDrivenMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Washington.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Washington
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900F5GTSJJHGE9287.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900F5GTSJJHGE9287
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OOTC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: OTHER OTC
type: Ontology Individual
---

# OTHER OTC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OOTC>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Washington](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Washington.md)
- **Related to**: [Facility-FINR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-FINR.md)
- **Related to**: [ServiceProvider-L-254900F5GTSJJHGE9287](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-254900F5GTSJJHGE9287.md)

## Annotations

- **label**: OTHER OTC
- **note**: OTC SECURITY THAT IS NOT QUOTED ON THE NNQS (PREVIOUSLY OTCBB) BUT IS ELIGIBLE FOR TRADE REPORTING TO THE TRADE REPORTING FACILITY, IS CATEGORIZED AS "OTHER-OTC".
- **hasFormalName**: OTHER OTC
- **hasWebsite**: http://www.otcbb.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
