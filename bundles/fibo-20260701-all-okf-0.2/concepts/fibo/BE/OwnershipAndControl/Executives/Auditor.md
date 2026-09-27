---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: auditor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party qualified and authorized to review and verify the accuracy of financial records and ensure that companies
      comply with tax laws
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An auditor is authorized to audit one or more specific organizations, i.e., by the authorizing party indicated
      by the situation.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An auditor may be an internal auditor - an individual whose primary job function is to audit his or her own company,
      or an external auditor - an individual from outside the company, who typically is employed by an auditing firm who handles
      many different clients.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/AuthorizedParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Auditor
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: auditor
type: Ontology Class
---

# auditor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Auditor>

## Definition

party qualified and authorized to review and verify the accuracy of financial records and ensure that companies comply with tax laws

## Relationships

- **Subclass of**: [AuthorizedParty](<https://www.omg.org/spec/Commons/BusinessAuthorizations/AuthorizedParty>)

## Annotations

- **label**: auditor
- **definition**: party qualified and authorized to review and verify the accuracy of financial records and ensure that companies comply with tax laws
- **explanatoryNote**: An auditor is authorized to audit one or more specific organizations, i.e., by the authorizing party indicated by the situation.
- **explanatoryNote**: An auditor may be an internal auditor - an individual whose primary job function is to audit his or her own company, or an external auditor - an individual from outside the company, who typically is employed by an auditing firm who handles many different clients.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
