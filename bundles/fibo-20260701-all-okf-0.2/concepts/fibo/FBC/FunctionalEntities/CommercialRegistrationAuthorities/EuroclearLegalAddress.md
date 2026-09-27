---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Euroclear SA/NV legal address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal address for Euroclear SA/NV
  - language: fr
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: Boulevard du Roi Albert II 1
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine2
    value: Saint-Josse-ten-Noode
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '1210'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Brussels.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Brussels
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Belgium
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/EuroclearLegalAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: Euroclear SA/NV legal address
type: Ontology Individual
---

# Euroclear SA/NV legal address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/EuroclearLegalAddress>

## Definition

legal address for Euroclear SA/NV

## Relationships

- **Related to**: [Belgium](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Belgium>)
- **Related to**: [Brussels](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Brussels.md)

## Annotations

- **label**: Euroclear SA/NV legal address
- **definition**: legal address for Euroclear SA/NV
- **hasAddressLine1** (fr): Boulevard du Roi Albert II 1
- **hasAddressLine2**: Saint-Josse-ten-Noode
- **hasPostalCode**: 1210

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
