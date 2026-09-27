---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NASDAQ - ALL MARKETS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NASDAQ
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NASDAQ - ALL MARKETS
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nasdaq.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300L8X1Q78ERXFD06.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300L8X1Q78ERXFD06
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NASDAQ - ALL MARKETS
type: Ontology Individual
---

# NASDAQ - ALL MARKETS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS>

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [ServiceProvider-L-549300L8X1Q78ERXFD06](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-549300L8X1Q78ERXFD06.md)

## Annotations

- **label**: NASDAQ - ALL MARKETS
- **hasFacilityAcronym**: NASDAQ
- **hasFormalName**: NASDAQ - ALL MARKETS
- **hasWebsite**: http://www.nasdaq.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
