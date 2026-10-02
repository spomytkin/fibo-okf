---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: external auditor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: independent party qualified and authorized to examine and report on the accuracy of financial records and ensure
      that companies comply with tax laws
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An external auditor is an individual or organization from outside the company, who typically is employed by an
      auditing firm that handles many different clients.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Auditor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Auditor
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExternalAuditor
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: external auditor
type: Ontology Class
---

# external auditor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExternalAuditor>

## Definition

independent party qualified and authorized to examine and report on the accuracy of financial records and ensure that companies comply with tax laws

## Relationships

- **Subclass of**: [Auditor](/concepts/fibo/BE/OwnershipAndControl/Executives/Auditor.md)

## Annotations

- **label**: external auditor
- **definition**: independent party qualified and authorized to examine and report on the accuracy of financial records and ensure that companies comply with tax laws
- **explanatoryNote**: An external auditor is an individual or organization from outside the company, who typically is employed by an auditing firm that handles many different clients.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
