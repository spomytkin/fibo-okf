---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: manager-managed limited liability company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: limited liability company in which the members appoint one or more managers to handle the daily operations and
      administrative responsibilities of the organization
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If no members are interested in managing the LLC, an external manager (someone who doesn't own any portion of the
      LLC) can be hired to run the business operations, including, in some jurisdictions, a third-party entity, such as another
      company.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagerManagedLimitedLiabilityCompany
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: manager-managed limited liability company
type: Ontology Class
---

# manager-managed limited liability company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/ManagerManagedLimitedLiabilityCompany>

## Definition

limited liability company in which the members appoint one or more managers to handle the daily operations and administrative responsibilities of the organization

## Relationships

- **Subclass of**: [LimitedLiabilityCompany](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany.md)

## Annotations

- **label**: manager-managed limited liability company
- **definition**: limited liability company in which the members appoint one or more managers to handle the daily operations and administrative responsibilities of the organization
- **explanatoryNote**: If no members are interested in managing the LLC, an external manager (someone who doesn't own any portion of the LLC) can be hired to run the business operations, including, in some jurisdictions, a third-party entity, such as another company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
