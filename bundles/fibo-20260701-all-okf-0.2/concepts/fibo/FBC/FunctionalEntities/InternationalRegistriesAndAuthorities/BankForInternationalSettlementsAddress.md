---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bank for International Settlements address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Tower building address for the Bank for International Settlements (BIS)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: Centralbahnplatz 2
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '4051'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Basel.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Basel
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: Bank for International Settlements address
type: Ontology Individual
---

# Bank for International Settlements address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress>

## Definition

Tower building address for the Bank for International Settlements (BIS)

## Relationships

- **Related to**: [Switzerland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Switzerland>)
- **Related to**: [Basel](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Basel.md)

## Annotations

- **label**: Bank for International Settlements address
- **definition**: Tower building address for the Bank for International Settlements (BIS)
- **hasAddressLine1**: Centralbahnplatz 2
- **hasPostalCode**: 4051

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
