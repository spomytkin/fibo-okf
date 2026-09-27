---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: New York Stock Exchange headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for the New York Stock Exchange
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 11 Wall Street
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '10005'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NewYork
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeHeadquartersAddress
sources:
- id: fibo-source-7c3670c0b0
  resource: references/fibo/EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
  sha256: 7c3670c0b01b44daf9d230ebaa0d7ca05831ee5103d2f94eabe7f3b40573ffd1
  title: FIBO source EXMP/LegalEntities/MarketsAndExchangesExamples.rdf
title: New York Stock Exchange headquarters address
type: Ontology Individual
---

# New York Stock Exchange headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/MarketsAndExchangesExamples/NewYorkStockExchangeHeadquartersAddress>

## Definition

headquarters address for the New York Stock Exchange

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [New_York](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/New_York.md)
- **Related to**: [NewYork](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NewYork>)

## Annotations

- **label**: New York Stock Exchange headquarters address
- **definition**: headquarters address for the New York Stock Exchange
- **hasAddressLine1**: 11 Wall Street
- **hasPostalCode**: 10005

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
