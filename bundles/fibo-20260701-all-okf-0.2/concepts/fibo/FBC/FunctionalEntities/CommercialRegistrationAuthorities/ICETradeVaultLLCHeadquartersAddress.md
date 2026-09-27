---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ICE Trade Vault, LLC headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for ICE Trade Vault, LLC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 5660 New Northside Drive
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '30328'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Atlanta.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Atlanta
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Georgia
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICETradeVaultLLCHeadquartersAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: ICE Trade Vault, LLC headquarters address
type: Ontology Individual
---

# ICE Trade Vault, LLC headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ICETradeVaultLLCHeadquartersAddress>

## Definition

headquarters address for ICE Trade Vault, LLC

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Atlanta](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Atlanta.md)
- **Related to**: [Georgia](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Georgia>)

## Annotations

- **label**: ICE Trade Vault, LLC headquarters address
- **definition**: headquarters address for ICE Trade Vault, LLC
- **hasAddressLine1**: 5660 New Northside Drive
- **hasPostalCode**: 30328

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
