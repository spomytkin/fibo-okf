---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has managing member
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a managing member in a controlling role of a limited liability company that has responsibility for the
      day-to-day business operations
  range:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/hasManagingMember
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: has managing member
type: Ontology Property
---

# has managing member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/hasManagingMember>

## Definition

indicates a managing member in a controlling role of a limited liability company that has responsibility for the day-to-day business operations

## Relationships

- **Range**: [ManagingMember](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember.md)
- **Subproperty of**: [hasControllingOrganizationMember](/concepts/fibo/BE/OwnershipAndControl/ControlParties/hasControllingOrganizationMember.md)

## Annotations

- **label**: has managing member
- **definition**: indicates a managing member in a controlling role of a limited liability company that has responsibility for the day-to-day business operations

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
