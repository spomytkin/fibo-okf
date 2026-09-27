---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: living trust
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trust created during an individual's lifetime where a designated person, the trustee, is given responsibility for
      managing that individual's assets for the benefit of the eventual beneficiary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A living trust is designed to allow for the easy transfer of the trust creator or settlor's assets while bypassing
      the often complex and expensive legal process of probate. Living trust agreements designate a trustee who holds legal
      possession of assets and property that flow into the trust.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trust.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/LivingTrust
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: living trust
type: Ontology Class
---

# living trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/LivingTrust>

## Definition

trust created during an individual's lifetime where a designated person, the trustee, is given responsibility for managing that individual's assets for the benefit of the eventual beneficiary

## Relationships

- **Subclass of**: [Trust](/concepts/fibo/BE/Trusts/Trusts/Trust.md)

## Annotations

- **label**: living trust
- **definition**: trust created during an individual's lifetime where a designated person, the trustee, is given responsibility for managing that individual's assets for the benefit of the eventual beneficiary
- **explanatoryNote**: A living trust is designed to allow for the easy transfer of the trust creator or settlor's assets while bypassing the often complex and expensive legal process of probate. Living trust agreements designate a trustee who holds legal possession of assets and property that flow into the trust.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
