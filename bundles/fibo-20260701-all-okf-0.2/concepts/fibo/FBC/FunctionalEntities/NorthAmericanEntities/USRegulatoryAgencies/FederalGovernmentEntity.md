---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: federal government entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal organization that is an independent agency, instrumentality or other permanent or semi-permanent organization
      in the machinery of government in the United States, authorized by the executive branch or by Congress, that operates
      at the national (federal) level
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  subclass_of:
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalGovernmentEntity
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: federal government entity
type: Ontology Class
---

# federal government entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalGovernmentEntity>

## Definition

formal organization that is an independent agency, instrumentality or other permanent or semi-permanent organization in the machinery of government in the United States, authorized by the executive branch or by Congress, that operates at the national (federal) level

## Relationships

- **Subclass of**: [GovernmentBody](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)

## Constraints

- **[hasJurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction`

## Annotations

- **label**: federal government entity
- **definition**: formal organization that is an independent agency, instrumentality or other permanent or semi-permanent organization in the machinery of government in the United States, authorized by the executive branch or by Congress, that operates at the national (federal) level

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
