---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractually capable entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a unique entity that is legally or financially responsible for the performance of financial transactions, or has
      the legal right in its jurisdiction to enter independently into legal contracts, regardless of whether it is incorporated
      or constituted in some other way (e.g. trust, partnership, contractual). This excludes natural persons, but includes
      governmental organizations and supranationals.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 17442
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Organizations/LegalEntity
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/ContractuallyCapableEntity
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: contractually capable entity
type: Ontology Class
---

# contractually capable entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/ContractuallyCapableEntity>

## Definition

a unique entity that is legally or financially responsible for the performance of financial transactions, or has the legal right in its jurisdiction to enter independently into legal contracts, regardless of whether it is incorporated or constituted in some other way (e.g. trust, partnership, contractual). This excludes natural persons, but includes governmental organizations and supranationals.

## Relationships

- **Subclass of**: [AgentRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/AgentRole>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: contractually capable entity
- **definition**: a unique entity that is legally or financially responsible for the performance of financial transactions, or has the legal right in its jurisdiction to enter independently into legal contracts, regardless of whether it is incorporated or constituted in some other way (e.g. trust, partnership, contractual). This excludes natural persons, but includes governmental organizations and supranationals.
- **adaptedFrom**: ISO 17442

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
