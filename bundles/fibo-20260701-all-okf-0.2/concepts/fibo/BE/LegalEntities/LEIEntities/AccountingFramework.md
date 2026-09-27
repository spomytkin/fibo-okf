---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: accounting framework
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: framework, including policies, methods, rules, and processes, used to measure, recognize, present, and disclose
      the information appearing in an entity's financial statements, and, from a legal ownership perspective, that is applied
      for accounting consolidation determination
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities/RelationshipQualifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipQualifier
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/AccountingFramework
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: accounting framework
type: Ontology Class
---

# accounting framework

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/AccountingFramework>

## Definition

framework, including policies, methods, rules, and processes, used to measure, recognize, present, and disclose the information appearing in an entity's financial statements, and, from a legal ownership perspective, that is applied for accounting consolidation determination

## Relationships

- **Subclass of**: [RelationshipQualifier](/concepts/fibo/BE/LegalEntities/LEIEntities/RelationshipQualifier.md)

## Annotations

- **label**: accounting framework
- **definition**: framework, including policies, methods, rules, and processes, used to measure, recognize, present, and disclose the information appearing in an entity's financial statements, and, from a legal ownership perspective, that is applied for accounting consolidation determination
- **adaptedFrom**: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
