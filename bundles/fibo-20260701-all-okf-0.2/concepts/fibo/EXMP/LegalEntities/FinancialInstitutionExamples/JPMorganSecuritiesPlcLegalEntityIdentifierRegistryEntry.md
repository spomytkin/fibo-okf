---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: JP Morgan Securities legal entity identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity identifier Global LEI Index registry entry for JP Morgan Securities
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '2012-06-06T08:53:00-07:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate
    value: '2025-12-12T06:54:59-08:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate
    value: '2026-12-28T07:20:38-08:00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
  related_to:
  - predicate: https://www.omg.org/spec/Commons/Collections/comprises
    resource: https://rdf.gleif.org/L1/L-K6Q0W1PS1L1O4IQL9C32-LEI
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganSecuritiesPlcLegalEntityIdentifierRegistryEntry
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: JP Morgan Securities legal entity identifier registry entry
type: Ontology Individual
---

# JP Morgan Securities legal entity identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/JPMorganSecuritiesPlcLegalEntityIdentifierRegistryEntry>

## Definition

legal entity identifier Global LEI Index registry entry for JP Morgan Securities

## Relationships

- **Related to**: [IssuedStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md)
- **Related to**: [EntityValidationLevelFullyCorroborated](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated.md)
- **Related to**: [L-K6Q0W1PS1L1O4IQL9C32-LEI](<https://rdf.gleif.org/L1/L-K6Q0W1PS1L1O4IQL9C32-LEI>)

## Annotations

- **label**: JP Morgan Securities legal entity identifier registry entry
- **definition**: legal entity identifier Global LEI Index registry entry for JP Morgan Securities
- **hasInitialRegistrationDate**: 2012-06-06T08:53:00-07:00
- **hasRegistrationRevisionDate**: 2025-12-12T06:54:59-08:00
- **hasRenewalDate**: 2026-12-28T07:20:38-08:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
