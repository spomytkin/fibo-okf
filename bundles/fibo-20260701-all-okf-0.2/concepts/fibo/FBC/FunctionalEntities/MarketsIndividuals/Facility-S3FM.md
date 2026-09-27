---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SOCIETY3 FUNDERSMART
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: NON REGULATED, US SEC AND SWISS FINMA COMPLIANT AND BANKING LICENSE EXEMPT EQUITY FUNDRAISING AND TRADING PLATFORM.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: S3FM
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SOCIETY3 FUNDERSMART
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://society3.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Luzern.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Luzern
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SOCIETY3FUNDERSMART.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SOCIETY3FUNDERSMART
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-S3FM
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SOCIETY3 FUNDERSMART
type: Ontology Individual
---

# SOCIETY3 FUNDERSMART

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-S3FM>

## Relationships

- **Related to**: [Switzerland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland>)
- **Related to**: [Luzern](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Luzern.md)
- **Related to**: [ServiceProvider-SOCIETY3FUNDERSMART](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SOCIETY3FUNDERSMART.md)

## Annotations

- **label**: SOCIETY3 FUNDERSMART
- **note**: NON REGULATED, US SEC AND SWISS FINMA COMPLIANT AND BANKING LICENSE EXEMPT EQUITY FUNDRAISING AND TRADING PLATFORM.
- **hasFacilityAcronym**: S3FM
- **hasFormalName**: SOCIETY3 FUNDERSMART
- **hasWebsite**: http://society3.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
