---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: benefit corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit corporation set up under specific state legislation, typically to provide some social benefit, without
      an obligation to maximize shareholder return
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is a US-specific type of non-profit corporation defined in recent legislation in a number of states. In California,
      for example, benefit corporations may be defined as public benefit or mutual benefit corporations, depending on their
      purpose.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/BenefitCorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: benefit corporation
type: Ontology Class
---

# benefit corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/BenefitCorporation>

## Definition

not-for-profit corporation set up under specific state legislation, typically to provide some social benefit, without an obligation to maximize shareholder return

## Relationships

- **Subclass of**: [NotForProfitCorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md)

## Annotations

- **label**: benefit corporation
- **definition**: not-for-profit corporation set up under specific state legislation, typically to provide some social benefit, without an obligation to maximize shareholder return
- **explanatoryNote**: This is a US-specific type of non-profit corporation defined in recent legislation in a number of states. In California, for example, benefit corporations may be defined as public benefit or mutual benefit corporations, depending on their purpose.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
