---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: London Stock Exchange plc. headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for London Stock Exchange plc.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 10 Paternoster Square
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: EC4M 7LS
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/London
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchangeHeadquartersAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: London Stock Exchange plc. headquarters address
type: Ontology Individual
---

# London Stock Exchange plc. headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchangeHeadquartersAddress>

## Definition

headquarters address for London Stock Exchange plc.

## Relationships

- **Related to**: [UnitedKingdomOfGreatBritainAndNorthernIreland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland>)
- **Related to**: [London](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md)

## Annotations

- **label**: London Stock Exchange plc. headquarters address
- **definition**: headquarters address for London Stock Exchange plc.
- **hasAddressLine1**: 10 Paternoster Square
- **hasPostalCode**: EC4M 7LS

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
