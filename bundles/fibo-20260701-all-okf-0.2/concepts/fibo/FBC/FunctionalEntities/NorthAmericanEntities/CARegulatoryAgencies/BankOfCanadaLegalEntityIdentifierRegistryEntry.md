---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bank of Canada legal entity identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity identifier for the Bank of Canada
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '2014-03-27T18:39:00-07:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate
    value: '2025-02-26T07:49:54-08:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate
    value: '2026-02-26T07:49:54-08:00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
  related_to:
  - predicate: https://www.omg.org/spec/Commons/Collections/comprises
    resource: https://rdf.gleif.org/L1/L-549300PN6MKI0CLP4T28-LEI
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelEntitySuppliedOnly.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelEntitySuppliedOnly
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanadaLegalEntityIdentifierRegistryEntry
sources:
- id: fibo-source-3a86c5f7dd
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
  sha256: 3a86c5f7dd7acfa3d8ca47686faffd64ac5f85eae9e50730e1337823edbfcda4
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
title: Bank of Canada legal entity identifier registry entry
type: Ontology Individual
---

# Bank of Canada legal entity identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanadaLegalEntityIdentifierRegistryEntry>

## Definition

legal entity identifier for the Bank of Canada

## Relationships

- **Related to**: [IssuedStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md)
- **Related to**: [EntityValidationLevelEntitySuppliedOnly](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelEntitySuppliedOnly.md)
- **Related to**: [L-549300PN6MKI0CLP4T28-LEI](<https://rdf.gleif.org/L1/L-549300PN6MKI0CLP4T28-LEI>)

## Annotations

- **label**: Bank of Canada legal entity identifier registry entry
- **definition**: legal entity identifier for the Bank of Canada
- **hasInitialRegistrationDate**: 2014-03-27T18:39:00-07:00
- **hasRegistrationRevisionDate**: 2025-02-26T07:49:54-08:00
- **hasRenewalDate**: 2026-02-26T07:49:54-08:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
