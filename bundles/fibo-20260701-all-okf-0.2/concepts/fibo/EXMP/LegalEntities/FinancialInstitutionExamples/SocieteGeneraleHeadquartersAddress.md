---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Société Générale headquarters address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters address for Société Générale
  - language: fr
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: 29 Boulevard Haussmann
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '75009'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/France
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleHeadquartersAddress
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Société Générale headquarters address
type: Ontology Individual
---

# Société Générale headquarters address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleHeadquartersAddress>

## Definition

headquarters address for Société Générale

## Relationships

- **Related to**: [France](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/France>)
- **Related to**: [Paris](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris.md)

## Annotations

- **label**: Société Générale headquarters address
- **definition**: headquarters address for Société Générale
- **hasAddressLine1** (fr): 29 Boulevard Haussmann
- **hasPostalCode**: 75009

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
