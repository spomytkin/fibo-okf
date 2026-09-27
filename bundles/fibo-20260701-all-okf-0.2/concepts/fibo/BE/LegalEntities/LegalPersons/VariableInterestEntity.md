---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable interest entity
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal entity whose shareholders are entitled to a percentage of a named company's profits via a private contract
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: VIE
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Variable interest entity (VIE) is a term used by the Financial Accounting Standards Board (FASB) to refer to a
      legal entity with certain characteristics such that a public company with a financial interest in the entity is subject
      to certain financial reporting requirements. Examples include certain Chinese companies, such as Alibaba, that leverage
      VIEs to gain access to foreign capital that would otherwise not be available due to Chinese government regulations.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: shell company
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/VariableInterestEntity
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: variable interest entity
type: Ontology Class
---

# variable interest entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/VariableInterestEntity>

## Definition

legal entity whose shareholders are entitled to a percentage of a named company's profits via a private contract

## Relationships

- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label** (en): variable interest entity
- **definition** (en): legal entity whose shareholders are entitled to a percentage of a named company's profits via a private contract
- **abbreviation** (en): VIE
- **explanatoryNote** (en): Variable interest entity (VIE) is a term used by the Financial Accounting Standards Board (FASB) to refer to a legal entity with certain characteristics such that a public company with a financial interest in the entity is subject to certain financial reporting requirements. Examples include certain Chinese companies, such as Alibaba, that leverage VIEs to gain access to foreign capital that would otherwise not be available due to Chinese government regulations.
- **synonym** (en): shell company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
