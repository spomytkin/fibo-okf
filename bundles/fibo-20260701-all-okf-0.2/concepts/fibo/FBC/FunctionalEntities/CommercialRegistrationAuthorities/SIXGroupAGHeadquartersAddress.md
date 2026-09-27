---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: SIX Group AG headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for SIX Group AG
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: Hardturmstrasse 201
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '8005'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Zurich.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Zurich
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAGHeadquartersAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: SIX Group AG headquarters address
type: Ontology Individual
---

# SIX Group AG headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXGroupAGHeadquartersAddress>

## Definition

headquarters address for SIX Group AG

## Relationships

- **Related to**: [Switzerland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland>)
- **Related to**: [Zurich](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Zurich.md)

## Annotations

- **label**: SIX Group AG headquarters address
- **definition**: headquarters address for SIX Group AG
- **hasAddressLine1**: Hardturmstrasse 201
- **hasPostalCode**: 8005

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
