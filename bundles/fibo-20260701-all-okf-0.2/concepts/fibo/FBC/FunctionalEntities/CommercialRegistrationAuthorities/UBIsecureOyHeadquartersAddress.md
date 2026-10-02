---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Ubisecure Oy headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for Ubisecure Oy
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: Tekniikantie 14
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '02150'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Espoo.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Espoo
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Finland
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-FI/FI-18-Subdivision
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/UBIsecureOyHeadquartersAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: Ubisecure Oy headquarters address
type: Ontology Individual
---

# Ubisecure Oy headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/UBIsecureOyHeadquartersAddress>

## Definition

headquarters address for Ubisecure Oy

## Relationships

- **Related to**: [Finland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Finland>)
- **Related to**: [Espoo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Espoo.md)
- **Related to**: [FI-18-Subdivision](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-FI/FI-18-Subdivision>)

## Annotations

- **label**: Ubisecure Oy headquarters address
- **definition**: headquarters address for Ubisecure Oy
- **hasAddressLine1**: Tekniikantie 14
- **hasPostalCode**: 02150

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
