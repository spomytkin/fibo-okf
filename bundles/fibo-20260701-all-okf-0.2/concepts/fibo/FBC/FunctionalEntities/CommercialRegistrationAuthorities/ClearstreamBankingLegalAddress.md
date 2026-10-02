---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Clearstream Banking S.A. legal address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal address for Clearstream Banking S.A.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 42, Avenue J.F. Kennedy
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: L-1855
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Luxembourg.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Luxembourg
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Luxembourg
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress
sources:
- id: fibo-source-7fb80db6c9
  resource: references/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
  sha256: 7fb80db6c9bf1521e4fd15a83716ed1dd7131e04cc3eab330d443c2f46cfa2aa
  title: FIBO source FBC/FunctionalEntities/CommercialRegistrationAuthorities.rdf
title: Clearstream Banking S.A. legal address
type: Ontology Individual
---

# Clearstream Banking S.A. legal address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/ClearstreamBankingLegalAddress>

## Definition

legal address for Clearstream Banking S.A.

## Relationships

- **Related to**: [Luxembourg](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Luxembourg>)
- **Related to**: [Luxembourg](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Luxembourg.md)

## Annotations

- **label**: Clearstream Banking S.A. legal address
- **definition**: legal address for Clearstream Banking S.A.
- **hasAddressLine1**: 42, Avenue J.F. Kennedy
- **hasPostalCode**: L-1855

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
