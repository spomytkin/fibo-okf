---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has registration status
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the status of a specific registration, such as for an identifier or license
  range:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has registration status
type: Ontology Property
---

# has registration status

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus>

## Definition

indicates the status of a specific registration, such as for an identifier or license

## Relationships

- **Range**: [RegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
- **Subproperty of**: [hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)

## Annotations

- **label**: has registration status
- **definition**: indicates the status of a specific registration, such as for an identifier or license

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
