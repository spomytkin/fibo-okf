---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: TAURUS TDX
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: TDX IS A SWISS ORGANIZED TRADING FACILITY (OTF), OPERATED BY TAURUS SA, A REGULATED SECURITIES FIRM AUTHORIZED
      AND SUPERVISED BY THE SWISS FINANCIAL MARKET AUTHORITY (FINMA).
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: TDX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: TAURUS TDX
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.t-dx.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OrganizedTradingFacility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Geneva.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Geneva
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-506700HJTJ42L5IJDG59.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-506700HJTJ42L5IJDG59
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-TDXS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: TAURUS TDX
type: Ontology Individual
---

# TAURUS TDX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-TDXS>

## Relationships

- **Related to**: [Switzerland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland>)
- **Related to**: [Geneva](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Geneva.md)
- **Related to**: [ServiceProvider-L-506700HJTJ42L5IJDG59](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-506700HJTJ42L5IJDG59.md)

## Annotations

- **label**: TAURUS TDX
- **note**: TDX IS A SWISS ORGANIZED TRADING FACILITY (OTF), OPERATED BY TAURUS SA, A REGULATED SECURITIES FIRM AUTHORIZED AND SUPERVISED BY THE SWISS FINANCIAL MARKET AUTHORITY (FINMA).
- **hasFacilityAcronym**: TDX
- **hasFormalName**: TAURUS TDX
- **hasWebsite**: http://www.t-dx.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
