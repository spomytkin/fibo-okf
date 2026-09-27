---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Global Legal Entity Identifier Foundation (GLEIF) legal entity identifier registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Global LEI Index registry entry for Global Legal Entity Identifier Foundation (GLEIF)
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasInitialRegistrationDate
    value: '2018-03-15T22:13:33-07:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationRevisionDate
    value: '2021-07-15T05:29:06-07:00'
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate
    value: '2022-03-15T16:00:00-07:00'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
  related_to:
  - predicate: https://www.omg.org/spec/Commons/Collections/comprises
    resource: https://rdf.gleif.org/L1/L-506700GE1G29325QX363-LEI
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasValidationLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GLEIFLegalEntityIdentifierRegistryEntry
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: Global Legal Entity Identifier Foundation (GLEIF) legal entity identifier registry entry
type: Ontology Individual
---

# Global Legal Entity Identifier Foundation (GLEIF) legal entity identifier registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/GLEIFLegalEntityIdentifierRegistryEntry>

## Definition

Global LEI Index registry entry for Global Legal Entity Identifier Foundation (GLEIF)

## Relationships

- **Related to**: [IssuedStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/IssuedStatus.md)
- **Related to**: [EntityValidationLevelFullyCorroborated](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevelFullyCorroborated.md)
- **Related to**: [L-506700GE1G29325QX363-LEI](<https://rdf.gleif.org/L1/L-506700GE1G29325QX363-LEI>)

## Annotations

- **label**: Global Legal Entity Identifier Foundation (GLEIF) legal entity identifier registry entry
- **definition**: Global LEI Index registry entry for Global Legal Entity Identifier Foundation (GLEIF)
- **hasInitialRegistrationDate**: 2018-03-15T22:13:33-07:00
- **hasRegistrationRevisionDate**: 2021-07-15T05:29:06-07:00
- **hasRenewalDate**: 2022-03-15T16:00:00-07:00

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
