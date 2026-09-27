---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited liability company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: private limited company that combines the pass through taxation of a sole proprietorship or partnership with the
      limited liability of a corporation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LLC
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole
    value: N54854411bac847428af9a0f57b38aa57
  subclass_of:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: limited liability company
type: Ontology Class
---

# limited liability company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompany>

## Definition

private limited company that combines the pass through taxation of a sole proprietorship or partnership with the limited liability of a corporation

## Relationships

- **Subclass of**: [PrivateCompanyWithLimitedLiability](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability.md)

## Constraints

- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: min qualified cardinality 0
- **[playsRole](<https://www.omg.org/spec/Commons/RolesAndCompositions/playsRole>)**: some values from value `N54854411bac847428af9a0f57b38aa57`

## Annotations

- **label**: limited liability company
- **definition**: private limited company that combines the pass through taxation of a sole proprietorship or partnership with the limited liability of a corporation
- **abbreviation**: LLC

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
