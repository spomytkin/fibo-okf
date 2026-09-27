---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is trustee of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifies the trust over which a trustee has some measure of control
  domain:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trustee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustee
  range:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trust.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/isTrusteeOf
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: is trustee of
type: Ontology Property
---

# is trustee of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/isTrusteeOf>

## Definition

identifies the trust over which a trustee has some measure of control

## Relationships

- **Domain**: [Trustee](/concepts/fibo/BE/Trusts/Trusts/Trustee.md)
- **Range**: [Trust](/concepts/fibo/BE/Trusts/Trusts/Trust.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: is trustee of
- **definition**: identifies the trust over which a trustee has some measure of control

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
