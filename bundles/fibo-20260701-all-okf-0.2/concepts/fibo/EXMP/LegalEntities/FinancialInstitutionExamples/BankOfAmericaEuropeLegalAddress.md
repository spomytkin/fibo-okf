---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bank of America Europe legal address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal address for Bank of America Europe
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: Two Park Place
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine2
    value: Hatch Street
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine3
    value: Dublin 2
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: D02 NP94
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/BankOfAmericaEuropeLegalAddress
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Bank of America Europe legal address
type: Ontology Individual
---

# Bank of America Europe legal address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/BankOfAmericaEuropeLegalAddress>

## Definition

legal address for Bank of America Europe

## Relationships

- **Related to**: [Ireland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Ireland>)
- **Related to**: [Dublin](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Dublin.md)

## Annotations

- **label**: Bank of America Europe legal address
- **definition**: legal address for Bank of America Europe
- **hasAddressLine1**: Two Park Place
- **hasAddressLine2**: Hatch Street
- **hasAddressLine3**: Dublin 2
- **hasPostalCode**: D02 NP94

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
