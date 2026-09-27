---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DUBAI GOLD AND COMMODITIES EXCHANGE DMCC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: DGCX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: DUBAI GOLD AND COMMODITIES EXCHANGE DMCC
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.dgcx.ae
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dubai.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Dubai
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DUBAIGOLDANDCOMMODITIESEXCHANGEDMCC.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DUBAIGOLDANDCOMMODITIESEXCHANGEDMCC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedArabEmirates
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DGCX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: DUBAI GOLD AND COMMODITIES EXCHANGE DMCC
type: Ontology Individual
---

# DUBAI GOLD AND COMMODITIES EXCHANGE DMCC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DGCX>

## Relationships

- **Related to**: [UnitedArabEmirates](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedArabEmirates>)
- **Related to**: [Dubai](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dubai.md)
- **Related to**: [ServiceProvider-DUBAIGOLDANDCOMMODITIESEXCHANGEDMCC](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DUBAIGOLDANDCOMMODITIESEXCHANGEDMCC.md)

## Annotations

- **label**: DUBAI GOLD AND COMMODITIES EXCHANGE DMCC
- **hasFacilityAcronym**: DGCX
- **hasFormalName**: DUBAI GOLD AND COMMODITIES EXCHANGE DMCC
- **hasWebsite**: http://www.dgcx.ae

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
