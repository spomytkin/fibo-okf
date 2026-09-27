---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has date of registration
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date on which the corporation has registered in some jurisdiction for regulatory and / or for tax
      purposes
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfRegistration
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: has date of registration
type: Ontology Property
---

# has date of registration

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfRegistration>

## Definition

indicates the date on which the corporation has registered in some jurisdiction for regulatory and / or for tax purposes

## Relationships

- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has date of registration
- **definition**: indicates the date on which the corporation has registered in some jurisdiction for regulatory and / or for tax purposes

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
