---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is ultimately consolidated by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that the entity considered the 'end node' or consolidating entity (parent) fully consolidates the accounting
      of the 'start node' (child) per the accounting rules specified, and is the most distant consolidating entity to that
      child in any applicable ownership hierarchy
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
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isUltimatelyConsolidatedBy
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: is ultimately consolidated by
type: Ontology Property
---

# is ultimately consolidated by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isUltimatelyConsolidatedBy>

## Definition

indicates that the entity considered the 'end node' or consolidating entity (parent) fully consolidates the accounting of the 'start node' (child) per the accounting rules specified, and is the most distant consolidating entity to that child in any applicable ownership hierarchy

## Relationships

- **Range**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Subproperty of**: [isConsolidatedBy](/concepts/fibo/BE/LegalEntities/LEIEntities/isConsolidatedBy.md)

## Annotations

- **label**: is ultimately consolidated by
- **definition**: indicates that the entity considered the 'end node' or consolidating entity (parent) fully consolidates the accounting of the 'start node' (child) per the accounting rules specified, and is the most distant consolidating entity to that child in any applicable ownership hierarchy
- **adaptedFrom**: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
