---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private company with limited liability
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: hybrid business entity having characteristics of both a corporation and a partnership or sole proprietorship (depending
      on how many owners there are)
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://en.wikipedia.org/wiki/Limited_liability_company#Overview
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A private company with limited liability, although a business entity, is not a corporation. The primary characteristic
      this legal form shares with a corporation is limited liability, and the primary characteristic it shares with a partnership
      is the availability of pass-through income taxation. It is often more flexible than a corporation, and it is well-suited
      for companies with a single owner.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability
sources:
- id: fibo-source-ed254b1923
  resource: references/fibo/BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
  sha256: ed254b1923d2aaa91861926940b56bbacc941588b902d6479417e85b06987c0d
  title: FIBO source BE/PrivateLimitedCompanies/PrivateLimitedCompanies.rdf
title: private company with limited liability
type: Ontology Class
---

# private company with limited liability

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/PrivateCompanyWithLimitedLiability>

## Definition

hybrid business entity having characteristics of both a corporation and a partnership or sole proprietorship (depending on how many owners there are)

## Relationships

- **Subclass of**: [BusinessEntity](/concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: private company with limited liability
- **definition**: hybrid business entity having characteristics of both a corporation and a partnership or sole proprietorship (depending on how many owners there are)
- **adaptedFrom**: https://en.wikipedia.org/wiki/Limited_liability_company#Overview
- **explanatoryNote**: A private company with limited liability, although a business entity, is not a corporation. The primary characteristic this legal form shares with a corporation is limited liability, and the primary characteristic it shares with a partnership is the availability of pass-through income taxation. It is often more flexible than a corporation, and it is well-suited for companies with a single owner.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
