---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private limited company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: private limited company whose shareholders' liability is limited to the capital they originally invested
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: Ltd.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Private limited companies are common in countries including the U.K., Ireland, and Canada. They have one or more
      members, also called shareholders or owners, who buy in through private sales. Directors are company employees who keep
      up with all administrative tasks and tax filings but do not need to be shareholders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateLimitedCompany
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: private limited company
type: Ontology Class
---

# private limited company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateLimitedCompany>

## Definition

private limited company whose shareholders' liability is limited to the capital they originally invested

## Relationships

- **Subclass of**: [PrivateCompanyWithLimitedLiability](/concepts/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability.md)

## Annotations

- **label**: private limited company
- **definition**: private limited company whose shareholders' liability is limited to the capital they originally invested
- **abbreviation**: Ltd.
- **explanatoryNote**: Private limited companies are common in countries including the U.K., Ireland, and Canada. They have one or more members, also called shareholders or owners, who buy in through private sales. Directors are company employees who keep up with all administrative tasks and tax filings but do not need to be shareholders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
