---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Wells Fargo & Company legal entity identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity identifier registry entry for Wells Fargo & Company
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '2012-06-06T15:52:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate
    value: '2021-10-06T19:01:52.884000'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate
    value: '2022-10-11T00:31:00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
  related_to:
  - predicate: https://www.omg.org/spec/Commons/Collections/comprises
    resource: https://rdf.gleif.org/L1/L-PBLD0EJDB5FWOLXP3B76-LEI
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelPartiallyCorroborated.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelPartiallyCorroborated
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompanyLegalEntityIdentifierRegistryEntry
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Wells Fargo & Company legal entity identifier registry entry
type: Ontology Individual
---

# Wells Fargo & Company legal entity identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/WellsFargoAndCompanyLegalEntityIdentifierRegistryEntry>

## Definition

legal entity identifier registry entry for Wells Fargo & Company

## Relationships

- **Related to**: [IssuedStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md)
- **Related to**: [EntityValidationLevelPartiallyCorroborated](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelPartiallyCorroborated.md)
- **Related to**: [L-PBLD0EJDB5FWOLXP3B76-LEI](<https://rdf.gleif.org/L1/L-PBLD0EJDB5FWOLXP3B76-LEI>)

## Annotations

- **label**: Wells Fargo & Company legal entity identifier registry entry
- **definition**: legal entity identifier registry entry for Wells Fargo & Company
- **hasInitialRegistrationDate**: 2012-06-06T15:52:00
- **hasRegistrationRevisionDate**: 2021-10-06T19:01:52.884000
- **hasRenewalDate**: 2022-10-11T00:31:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
