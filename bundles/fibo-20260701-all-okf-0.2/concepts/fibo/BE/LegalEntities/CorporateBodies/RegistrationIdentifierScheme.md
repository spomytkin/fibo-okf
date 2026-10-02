---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registration identifier scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheme that defines the registration identifier per the issuing registration authority
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifierScheme
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: registration identifier scheme
type: Ontology Class
---

# registration identifier scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifierScheme>

## Definition

scheme that defines the registration identifier per the issuing registration authority

## Relationships

- **Subclass of**: [OrganizationIdentificationScheme](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [RegistrationIdentifier](/concepts/fibo/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md)

## Annotations

- **label**: registration identifier scheme
- **definition**: scheme that defines the registration identifier per the issuing registration authority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
