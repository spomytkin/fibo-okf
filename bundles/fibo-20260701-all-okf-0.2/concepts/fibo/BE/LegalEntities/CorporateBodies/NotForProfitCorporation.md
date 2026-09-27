---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: not-for-profit corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporation approved by its jurisdictional oversight and tax authorities as operating for educational, charitable,
      social, religious, civic or humanitarian purposes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A not-for-profit corporation is formed by incorporators, and has a board of directors and officers, but no shareholders.
      These incorporators, directors and officers may not receive a distribution of (any money from) profits, but officers
      and management may be paid reasonable salaries for services to the corporation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: non-profit corporation
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: not-for-profit corporation
type: Ontology Class
---

# not-for-profit corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation>

## Definition

corporation approved by its jurisdictional oversight and tax authorities as operating for educational, charitable, social, religious, civic or humanitarian purposes

## Relationships

- **Subclass of**: [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)
- **Subclass of**: [NotForProfitOrganization](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md)

## Annotations

- **label**: not-for-profit corporation
- **definition**: corporation approved by its jurisdictional oversight and tax authorities as operating for educational, charitable, social, religious, civic or humanitarian purposes
- **explanatoryNote**: A not-for-profit corporation is formed by incorporators, and has a board of directors and officers, but no shareholders. These incorporators, directors and officers may not receive a distribution of (any money from) profits, but officers and management may be paid reasonable salaries for services to the corporation.
- **synonym**: non-profit corporation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
