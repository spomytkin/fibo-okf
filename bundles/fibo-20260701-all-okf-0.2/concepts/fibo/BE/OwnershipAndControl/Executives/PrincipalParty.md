---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: principal party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: controlling party that is responsible for the management of daily business operations of an organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Signatory
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/PrincipalParty
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: principal party
type: Ontology Class
---

# principal party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/PrincipalParty>

## Definition

controlling party that is responsible for the management of daily business operations of an organization

## Relationships

- **Subclass of**: [Signatory](/concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Annotations

- **label**: principal party
- **definition**: controlling party that is responsible for the management of daily business operations of an organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
