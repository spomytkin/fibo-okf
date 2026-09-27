---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is constituted by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the instrument by which an entity is incorporated
  domain:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  range:
  - concept: /concepts/fibo/FND/Law/LegalCore/Constitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Constitution
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isConstitutedBy
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: is constituted by
type: Ontology Property
---

# is constituted by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isConstitutedBy>

## Definition

the instrument by which an entity is incorporated

## Relationships

- **Domain**: [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)
- **Range**: [Constitution](/concepts/fibo/FND/Law/LegalCore/Constitution.md)

## Annotations

- **label**: is constituted by
- **definition**: the instrument by which an entity is incorporated

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
