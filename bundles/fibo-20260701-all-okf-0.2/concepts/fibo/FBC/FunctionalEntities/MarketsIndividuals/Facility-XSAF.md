---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: JSE EQUITY DERIVATIVES MARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SAFEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: JSE EQUITY DERIVATIVES MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.safex.co.za
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Johannesburg.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Johannesburg
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XJSE.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XJSE
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-JSEEQUITYDERIVATIVESMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-JSEEQUITYDERIVATIVESMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/SouthAfrica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSAF
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: JSE EQUITY DERIVATIVES MARKET
type: Ontology Individual
---

# JSE EQUITY DERIVATIVES MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XSAF>

## Relationships

- **Related to**: [SouthAfrica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/SouthAfrica>)
- **Related to**: [Johannesburg](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Johannesburg.md)
- **Related to**: [Facility-XJSE](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XJSE.md)
- **Related to**: [ServiceProvider-JSEEQUITYDERIVATIVESMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-JSEEQUITYDERIVATIVESMARKET.md)

## Annotations

- **label**: JSE EQUITY DERIVATIVES MARKET
- **hasFacilityAcronym**: SAFEX
- **hasFormalName**: JSE EQUITY DERIVATIVES MARKET
- **hasWebsite**: http://www.safex.co.za

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
