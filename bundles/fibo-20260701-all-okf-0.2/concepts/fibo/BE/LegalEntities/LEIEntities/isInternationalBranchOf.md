---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is an international branch of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that the entity considered the 'start node' or consolidated entity (child) is an international subsidiary
      of the 'end node' (parent) in the jurisdiction of the child
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities/isConsolidatedBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isConsolidatedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isInternationalBranchOf
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: is an international branch of
type: Ontology Property
---

# is an international branch of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isInternationalBranchOf>

## Definition

indicates that the entity considered the 'start node' or consolidated entity (child) is an international subsidiary of the 'end node' (parent) in the jurisdiction of the child

## Relationships

- **Range**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Subproperty of**: [isConsolidatedBy](/concepts/fibo/BE/LegalEntities/LEIEntities/isConsolidatedBy.md)

## Annotations

- **label**: is an international branch of
- **definition**: indicates that the entity considered the 'start node' or consolidated entity (child) is an international subsidiary of the 'end node' (parent) in the jurisdiction of the child
- **adaptedFrom**: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
