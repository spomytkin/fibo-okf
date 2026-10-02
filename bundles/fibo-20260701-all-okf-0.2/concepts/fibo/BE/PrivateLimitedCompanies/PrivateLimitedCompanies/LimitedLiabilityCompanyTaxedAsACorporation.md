---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited liability company taxed as a corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: limited liability company that has elected to have corporate tax status
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: C-LLC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, LLCs that elect to be taxed as a corporation do so by filing an IRS Form 8832.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyTaxedAsACorporation
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: limited liability company taxed as a corporation
type: Ontology Class
---

# limited liability company taxed as a corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyTaxedAsACorporation>

## Definition

limited liability company that has elected to have corporate tax status

## Relationships

- **Subclass of**: [LimitedLiabilityCompany](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany.md)

## Annotations

- **label**: limited liability company taxed as a corporation
- **definition**: limited liability company that has elected to have corporate tax status
- **abbreviation**: C-LLC
- **explanatoryNote**: In the United States, LLCs that elect to be taxed as a corporation do so by filing an IRS Form 8832.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
