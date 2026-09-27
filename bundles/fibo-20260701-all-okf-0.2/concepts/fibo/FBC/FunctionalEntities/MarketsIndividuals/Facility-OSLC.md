---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SIX X-CLEAR AG
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SECURITIES LENDING, TRADE REGISTRATIONS AND FINANCIAL SETTLEMENT FOR DERIVATIVES. AS OF 1 MAY 2015 OSLO CLEARING
      ASA IS LEGALLY INTEGRATED INTO SIX X-CLEAR LTD.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: SIX X-CLEAR AG
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.six-securities-services.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Oslo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Oslo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SIXX-CLEARAG.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SIXX-CLEARAG
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Norway
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OSLC
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: SIX X-CLEAR AG
type: Ontology Individual
---

# SIX X-CLEAR AG

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OSLC>

## Relationships

- **Related to**: [Norway](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Norway>)
- **Related to**: [Oslo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Oslo.md)
- **Related to**: [ServiceProvider-SIXX-CLEARAG](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-SIXX-CLEARAG.md)

## Annotations

- **label**: SIX X-CLEAR AG
- **note**: SECURITIES LENDING, TRADE REGISTRATIONS AND FINANCIAL SETTLEMENT FOR DERIVATIVES. AS OF 1 MAY 2015 OSLO CLEARING ASA IS LEGALLY INTEGRATED INTO SIX X-CLEAR LTD.
- **hasFormalName**: SIX X-CLEAR AG
- **hasWebsite**: http://www.six-securities-services.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
