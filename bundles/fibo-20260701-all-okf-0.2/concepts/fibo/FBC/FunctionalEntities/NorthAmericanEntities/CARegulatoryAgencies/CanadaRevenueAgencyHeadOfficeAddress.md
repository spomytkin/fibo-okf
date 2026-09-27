---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Canada Revenue Agency head office address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: head office address for the Canada Revenue Agency
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 555 Mackenzie Avenue
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: K1A 0L5
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Ottawa.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Ottawa
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CA/Ontario
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CanadaRevenueAgencyHeadOfficeAddress
sources:
- id: fibo-source-3a86c5f7dd
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
  sha256: 3a86c5f7dd7acfa3d8ca47686faffd64ac5f85eae9e50730e1337823edbfcda4
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
title: Canada Revenue Agency head office address
type: Ontology Individual
---

# Canada Revenue Agency head office address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CanadaRevenueAgencyHeadOfficeAddress>

## Definition

head office address for the Canada Revenue Agency

## Relationships

- **Defined by**: [CARegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md)
- **Related to**: [Canada](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Canada>)
- **Related to**: [Ottawa](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Ottawa.md)
- **Related to**: [Ontario](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-CA/Ontario>)

## Annotations

- **label**: Canada Revenue Agency head office address
- **definition**: head office address for the Canada Revenue Agency
- **hasAddressLine1**: 555 Mackenzie Avenue
- **hasPostalCode**: K1A 0L5

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
