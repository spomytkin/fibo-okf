---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is consolidated by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the entity considered the 'end node' or consolidating entity (parent) from an ISO 17442 perspective
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isConsolidatedBy
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: is consolidated by
type: Ontology Property
---

# is consolidated by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isConsolidatedBy>

## Definition

indicates the entity considered the 'end node' or consolidating entity (parent) from an ISO 17442 perspective

## Relationships

- **Range**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: is consolidated by
- **definition**: indicates the entity considered the 'end node' or consolidating entity (parent) from an ISO 17442 perspective
- **adaptedFrom**: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
