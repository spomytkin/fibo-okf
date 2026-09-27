---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: relationship qualifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a classifier that qualifies something about the relationship between consolidated entities during the reporting
      period, such as the accounting framework used
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipQualifier
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: relationship qualifier
type: Ontology Class
---

# relationship qualifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipQualifier>

## Definition

a classifier that qualifies something about the relationship between consolidated entities during the reporting period, such as the accounting framework used

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: relationship qualifier
- **definition**: a classifier that qualifies something about the relationship between consolidated entities during the reporting period, such as the accounting framework used
- **adaptedFrom**: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
