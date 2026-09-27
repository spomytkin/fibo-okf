---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is managing member of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the controlled limited liability company that the managing member runs
  domain:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember
  inverse_of:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/hasManagingMember.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/hasManagingMember
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/isControllingMemberOf
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/isManagingMemberOf
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: is managing member of
type: Ontology Property
---

# is managing member of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/isManagingMemberOf>

## Definition

indicates the controlled limited liability company that the managing member runs

## Relationships

- **Domain**: [ManagingMember](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember.md)
- **Inverse of**: [hasManagingMember](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/hasManagingMember.md)
- **Subproperty of**: [isControllingMemberOf](/concepts/fibo/BE/OwnershipAndControl/ControlParties/isControllingMemberOf.md)

## Annotations

- **label**: is managing member of
- **definition**: indicates the controlled limited liability company that the managing member runs

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
