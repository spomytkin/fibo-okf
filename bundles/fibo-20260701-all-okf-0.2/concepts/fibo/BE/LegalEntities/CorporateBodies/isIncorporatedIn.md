---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is incorporated in
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the legal jurisdiction under which the legal entity is incorporated
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It is the laws of this jurisdiction that cause and allow the legal entity to exist and to incur debt and be sued
      at law as a legal entity.
  domain:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/isOrganizedIn
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: is incorporated in
type: Ontology Property
---

# is incorporated in

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/isIncorporatedIn>

## Definition

the legal jurisdiction under which the legal entity is incorporated

## Relationships

- **Domain**: [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)
- **Range**: [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **Subproperty of**: [isOrganizedIn](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isOrganizedIn>)

## Annotations

- **label**: is incorporated in
- **definition**: the legal jurisdiction under which the legal entity is incorporated
- **explanatoryNote**: It is the laws of this jurisdiction that cause and allow the legal entity to exist and to incur debt and be sued at law as a legal entity.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
