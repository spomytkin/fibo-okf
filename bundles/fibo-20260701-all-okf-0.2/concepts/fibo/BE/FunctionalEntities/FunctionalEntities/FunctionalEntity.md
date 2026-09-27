---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: functional entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party defined in terms of a function they or it performs
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/FunctionalRole
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: functional entity
type: Ontology Class
---

# functional entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity>

## Definition

party defined in terms of a function they or it performs

## Relationships

- **Subclass of**: [FunctionalRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/FunctionalRole>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: min qualified cardinality 0 of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Annotations

- **label**: functional entity
- **definition**: party defined in terms of a function they or it performs

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
