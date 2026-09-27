---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: STOCK EXCHANGE SAINT PETERSBURG
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: SPBEX
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: STOCK EXCHANGE SAINT PETERSBURG
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.spbex.ru
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Petersburg.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Petersburg
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-253400T8G8SXRUHTL526.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-253400T8G8SXRUHTL526
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPET
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: STOCK EXCHANGE SAINT PETERSBURG
type: Ontology Individual
---

# STOCK EXCHANGE SAINT PETERSBURG

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPET>

## Relationships

- **Related to**: [RussianFederation](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/RussianFederation>)
- **Related to**: [Saint_Petersburg](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Saint_Petersburg.md)
- **Related to**: [ServiceProvider-L-253400T8G8SXRUHTL526](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-253400T8G8SXRUHTL526.md)

## Annotations

- **label**: STOCK EXCHANGE SAINT PETERSBURG
- **hasFacilityAcronym**: SPBEX
- **hasFormalName**: STOCK EXCHANGE SAINT PETERSBURG
- **hasWebsite**: http://www.spbex.ru

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
