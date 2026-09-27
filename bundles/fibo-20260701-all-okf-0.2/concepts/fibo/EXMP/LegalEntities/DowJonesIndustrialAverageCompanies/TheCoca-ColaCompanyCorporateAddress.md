---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: The Coca-Cola Company corporate address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration address for The Coca-Cola Company
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: One Coca-Cola Plaza
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '30313'
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
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheCoca-ColaCompanyCorporateAddress
sources:
- id: fibo-source-c449487789
  resource: references/fibo/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
  sha256: c4494877893c93f9a616fa9cf3906eba0fb6c3a876878b1cdb60c40b3044436d
  title: FIBO source EXMP/LegalEntities/DowJonesIndustrialAverageCompanies.rdf
title: The Coca-Cola Company corporate address
type: Ontology Individual
---

# The Coca-Cola Company corporate address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/DowJonesIndustrialAverageCompanies/TheCoca-ColaCompanyCorporateAddress>

## Definition

registration address for The Coca-Cola Company

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Atlanta](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Atlanta.md)
- **Related to**: [Georgia](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/Georgia>)

## Annotations

- **label**: The Coca-Cola Company corporate address
- **definition**: registration address for The Coca-Cola Company
- **hasAddressLine1**: One Coca-Cola Plaza
- **hasPostalCode**: 30313

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
