---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: managing member
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: owner of an interest in a limited liability company who also runs the day-to-day business operations
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/isManagingMemberOf
    value: N2d55580820594bdb967f6443402d0092
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/PrincipalParty
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: managing member
type: Ontology Class
---

# managing member

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagingMember>

## Definition

owner of an interest in a limited liability company who also runs the day-to-day business operations

## Relationships

- **Subclass of**: [PrincipalParty](/concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md)
- **Subclass of**: [LimitedLiabilityCompanyMember](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyMember.md)

## Constraints

- **[isManagingMemberOf](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/isManagingMemberOf.md)**: some values from value `N2d55580820594bdb967f6443402d0092`

## Annotations

- **label**: managing member
- **definition**: owner of an interest in a limited liability company who also runs the day-to-day business operations

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
