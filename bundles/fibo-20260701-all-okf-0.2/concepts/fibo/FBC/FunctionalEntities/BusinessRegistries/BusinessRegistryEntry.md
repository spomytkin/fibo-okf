---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a business registry
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: business registry entry
type: Ontology Class
---

# business registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry>

## Definition

entry in a business registry

## Relationships

- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[hasRegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus.md)**: max qualified cardinality 1 of type [RegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [RegistrationIdentifier](/concepts/fibo/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md)
- **[hasRegistrationDate](<https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate>)**: some values from of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: business registry entry
- **definition**: entry in a business registry

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
