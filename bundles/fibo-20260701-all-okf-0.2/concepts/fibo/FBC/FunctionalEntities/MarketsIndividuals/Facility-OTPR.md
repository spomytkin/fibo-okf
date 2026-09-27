---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: OTP BANK ROMANIA SA
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: OTC MARKETS FOR OTP BANK ROMANIA.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: OTP BANK ROMANIA SA
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.otpbank.ro
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bucharest.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Bucharest
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5299003TM0P7W8DNUF61.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5299003TM0P7W8DNUF61
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Romania
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OTPR
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: OTP BANK ROMANIA SA
type: Ontology Individual
---

# OTP BANK ROMANIA SA

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-OTPR>

## Relationships

- **Related to**: [Romania](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Romania>)
- **Related to**: [Bucharest](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Bucharest.md)
- **Related to**: [ServiceProvider-L-5299003TM0P7W8DNUF61](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-5299003TM0P7W8DNUF61.md)

## Annotations

- **label**: OTP BANK ROMANIA SA
- **note**: OTC MARKETS FOR OTP BANK ROMANIA.
- **hasFormalName**: OTP BANK ROMANIA SA
- **hasWebsite**: http://www.otpbank.ro

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
