---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: The Depository Trust & Clearing Corporation headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for the The Depository Trust & Clearing Corporation
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 570 Washington Boulevard
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '07310'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NewJersey
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCHeadquartersAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: The Depository Trust & Clearing Corporation headquarters address
type: Ontology Individual
---

# The Depository Trust & Clearing Corporation headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/DTCCHeadquartersAddress>

## Definition

headquarters address for the The Depository Trust & Clearing Corporation

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Jersey_City](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Jersey_City.md)
- **Related to**: [NewJersey](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NewJersey>)

## Annotations

- **label**: The Depository Trust & Clearing Corporation headquarters address
- **definition**: headquarters address for the The Depository Trust & Clearing Corporation
- **hasAddressLine1**: 570 Washington Boulevard
- **hasPostalCode**: 07310

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
