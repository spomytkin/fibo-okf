---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MIAX FUTURES EXCHANGE - OCC CLEARING
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MIC USED FOR MIAX FUTURES EXCHANGE PRODUCTS CLEARED AT OCC.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: XMFE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: MIAX FUTURES EXCHANGE - OCC CLEARING
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.miaxglobal.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DesignatedContractMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Minneapolis.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Minneapolis
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMGE.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMGE
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300RGCVWZUN04IA69.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300RGCVWZUN04IA69
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMFE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: MIAX FUTURES EXCHANGE - OCC CLEARING
type: Ontology Individual
---

# MIAX FUTURES EXCHANGE - OCC CLEARING

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMFE>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Minneapolis](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Minneapolis.md)
- **Related to**: [Facility-XMGE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XMGE.md)
- **Related to**: [ServiceProvider-L-549300RGCVWZUN04IA69](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300RGCVWZUN04IA69.md)

## Annotations

- **label**: MIAX FUTURES EXCHANGE - OCC CLEARING
- **note**: MIC USED FOR MIAX FUTURES EXCHANGE PRODUCTS CLEARED AT OCC.
- **hasFacilityAcronym**: XMFE
- **hasFormalName**: MIAX FUTURES EXCHANGE - OCC CLEARING
- **hasWebsite**: http://www.miaxglobal.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
