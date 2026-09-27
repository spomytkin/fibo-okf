---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Wells Fargo Bank, National Association headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration address identified as the headquarters address for Wells Fargo Bank, National Association
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 301 South College Street
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '28202'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Charlotte.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Charlotte
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica
  - predicate: https://www.omg.org/spec/Commons/Locations/hasSubdivision
    resource: https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NorthCarolina
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoBankNationalAssociationHeadquartersAddress
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Wells Fargo Bank, National Association headquarters address
type: Ontology Individual
---

# Wells Fargo Bank, National Association headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoBankNationalAssociationHeadquartersAddress>

## Definition

registration address identified as the headquarters address for Wells Fargo Bank, National Association

## Relationships

- **Related to**: [UnitedStatesOfAmerica](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedStatesOfAmerica>)
- **Related to**: [Charlotte](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Charlotte.md)
- **Related to**: [NorthCarolina](<https://www.omg.org/spec/LCC/Countries/Regions/ISO3166-2-SubdivisionCodes-US/NorthCarolina>)

## Annotations

- **label**: Wells Fargo Bank, National Association headquarters address
- **definition**: registration address identified as the headquarters address for Wells Fargo Bank, National Association
- **hasAddressLine1**: 301 South College Street
- **hasPostalCode**: 28202

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
