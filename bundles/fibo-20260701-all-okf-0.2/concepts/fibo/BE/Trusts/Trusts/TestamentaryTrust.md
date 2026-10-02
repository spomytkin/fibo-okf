---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: testamentary trust
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trust established in accordance with the instructions contained in a last will and testament
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A will could have more than one testamentary trust. The trustee named is responsible for managing and distributing
      the trustor's assets to the beneficiaries as directed in the will. Sometimes called a will trust, the testamentary trust
      is irrevocable.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/Trusts/Trusts/IrrevocableTrust.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/IrrevocableTrust
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TestamentaryTrust
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: testamentary trust
type: Ontology Class
---

# testamentary trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TestamentaryTrust>

## Definition

trust established in accordance with the instructions contained in a last will and testament

## Relationships

- **Subclass of**: [IrrevocableTrust](/concepts/fibo/BE/Trusts/Trusts/IrrevocableTrust.md)

## Annotations

- **label**: testamentary trust
- **definition**: trust established in accordance with the instructions contained in a last will and testament
- **explanatoryNote**: A will could have more than one testamentary trust. The trustee named is responsible for managing and distributing the trustor's assets to the beneficiaries as directed in the will. Sometimes called a will trust, the testamentary trust is irrevocable.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
