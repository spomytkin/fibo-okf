---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Society for Worldwide Interbank Financial Telecommunication (SWIFT) legal entity identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Global LEI Index registry entry for the Society for Worldwide Interbank Financial Telecommunication (SWIFT)
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '2012-06-06T08:54:00-07:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate
    value: '2021-02-12T13:35:00-08:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate
    value: '2022-01-20T00:21:00-08:00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
  related_to:
  - predicate: https://www.omg.org/spec/Commons/Collections/comprises
    resource: https://rdf.gleif.org/L1/L-HB7FFAZI0OMZ8PP8OE26-LEI
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SWIFTLegalEntityIdentifierRegistryEntry
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: Society for Worldwide Interbank Financial Telecommunication (SWIFT) legal entity identifier registry entry
type: Ontology Individual
---

# Society for Worldwide Interbank Financial Telecommunication (SWIFT) legal entity identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/SWIFTLegalEntityIdentifierRegistryEntry>

## Definition

Global LEI Index registry entry for the Society for Worldwide Interbank Financial Telecommunication (SWIFT)

## Relationships

- **Related to**: [IssuedStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md)
- **Related to**: [EntityValidationLevelFullyCorroborated](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated.md)
- **Related to**: [L-HB7FFAZI0OMZ8PP8OE26-LEI](<https://rdf.gleif.org/L1/L-HB7FFAZI0OMZ8PP8OE26-LEI>)

## Annotations

- **label**: Society for Worldwide Interbank Financial Telecommunication (SWIFT) legal entity identifier registry entry
- **definition**: Global LEI Index registry entry for the Society for Worldwide Interbank Financial Telecommunication (SWIFT)
- **hasInitialRegistrationDate**: 2012-06-06T08:54:00-07:00
- **hasRegistrationRevisionDate**: 2021-02-12T13:35:00-08:00
- **hasRenewalDate**: 2022-01-20T00:21:00-08:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
